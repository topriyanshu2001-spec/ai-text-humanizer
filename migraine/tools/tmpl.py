import re, sys
sys.path.insert(0,"..")
from tellscan import words, mean

FW = set("""a an the of in on at to for from by with without within into onto over under
and or but nor so yet than then that which who whom whose this these those there here
is are was were be been being has have had do does did can could may might must should would will
as if when while after before during against between among per about across not no
its their his her our your it they we he she i one two three both each all some any more most less
than vs versus against""".split())

def clauses(text):
    out=[]
    for s in re.split(r"(?<=[.!?])\s+", text):
        for c in re.split(r"[;:,]\s+|\s+(?:and|but|or|which|while|whereas)\s+", s):
            w=words(c)
            if len(w)>=4: out.append(c)
    return out

def skeleton(clause):
    """Keep function words and slot-markers; replace content words with POS-ish slots."""
    toks=[]
    for raw in re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+(?:\.\d+)?%?|\[\d+[^\]]*\]", clause):
        low=raw.lower()
        if re.match(r"^\d", raw): toks.append("#")
        elif raw.startswith("["): toks.append("@")
        elif low in FW: toks.append(low)
        else: toks.append("W")
    return toks

def ngrams(seq,n):
    return [tuple(seq[i:i+n]) for i in range(len(seq)-n+1)]

def template_score(blocks, n=4):
    """Share of skeleton n-grams that recur across clauses. Higher = more templated."""
    from collections import Counter
    allng=Counter(); tot=0
    for b in blocks:
        for c in clauses(b):
            sk=skeleton(c)
            for g in ngrams(sk,n):
                allng[g]+=1; tot+=1
    if not tot: return 0.0,0
    rep=sum(v for v in allng.values() if v>1)
    return rep/tot, tot

def pair_similarity(blocks):
    """Mean max Jaccard similarity of skeleton n-gram sets between clause pairs inside the
    same block -- measures parallel construction locally, not across the whole document."""
    vals=[]
    for b in blocks:
        cs=[set(ngrams(skeleton(c),3)) for c in clauses(b)]
        cs=[c for c in cs if c]
        for i in range(len(cs)):
            best=0.0
            for j in range(len(cs)):
                if i==j: continue
                u=len(cs[i]|cs[j])
                if u: best=max(best, len(cs[i]&cs[j])/u)
            if len(cs)>1: vals.append(best)
    return mean(vals), len(vals)
