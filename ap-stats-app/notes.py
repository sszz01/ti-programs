NOTES = {
    "Desc Data": {
        "Concepts": {
            "SOCS": "Shape(Sym/Skew/Uni/Bi), Outliers, Ctr(mu/Med), Spread(s/IQR/Rng)",
            "Compare": "Use SOCS + Comp Lang (<,>,~)",
            "Center": "Med(mid, Q2), Mean(mu,x̄, avg), Mode(most)",
            "Spread": "Rng(Max-Min), IQR(Q3-Q1), SD(s,s, typ dev from mu), Var(s^2,s^2)",
            "Resist": "Med, IQR | NonRes: Mean, SD, Rng, Var, r, LSRL, R^2",
            "Mean<>Med": "Sym(~), SkR(mu>Med), SkL(mu<Med). mu pulled by skew.",
            "Boxplot": "5Num(Min,Q1,Med,Q3,Max). Out > 1.5IQR. Whisk->in fence"
        }
    },
    "Lin Reg": {
        "Concepts": {
            "Scatter": "Dir(+/-), Form(Lin/...), Str(W/M/S), Outliers",
            "r": "Corr. Lin Str/Dir. -1<=r<=1. No units.",
            "LSRL": "ŷ=a+bx. Min Se^2. x(Expl) y(Resp).",
            "Resid": "e = y-ŷ (Act-Pred). Se=0. Plot: No pattern -> Lin OK",
            "R^2": "% var y explained by LSRL(x,y)",
            "Interpret": "b: Per 1x, ŷ change by b. r: Str,Dir,Lin assoc. R^2: %var y expl.",
            "Caution": "Extrap(Bad!). Influential(change LSRL). Outlier(large e)."
        }
    },
    "Data Coll": {
        "Concepts": {
            "Samp Meth": "SRS, Strat(Grp->SRS), Clust(Loc->All), Syst(kth)",
            "Bias": "Vol, Conv, UnderCov, NonResp, Resp, Wording",
            "Study": "Obs(watch) vs Exp(treat)",
            "Exp Design": "Units, Factor(ExplVar), Level, RespVar, Treatmt",
            "Exp Princ": "Control(const), Replicate(many), Randomize(assign)",
            "Exp Types": "CRD, Block(decrease Var), MatchedPairs(dep)"
        }
    },
    "Probability": {
        "Concepts": {
            "Basics": "0<=P<=1. P(S)=1. P(Ac)=1-P(A).",
            "Events": "Union(AUB,or), Inter(AnB,and), MutEx/Disj(AnB=empty)",
            "Cond Prob": "P(A|B)=P(AnB)/P(B). Indep if P(A|B)=P(A)",
            "Rules": "Add: P(AUB)=P(A)+P(B)-P(AnB). Mult: P(AnB)=P(A)P(B)[if Indep]",
            "RV": "RandVar. Disc(count) / Cont(measure). E(X)=mu=Sum xip_i"
        }
    },
    "Distributions": {
        "Concepts": {
            "Binomial": "BINS: Bin(2),Indep,N(fix#),SuccP(same). X=#Succ. Calc: pdf(P(X=x)), cdf(P(X<=x))\n1 - binomialcdf(n, p, (x -1)) = cumulative outcome P(X >= x)",
            "Geometric": "BITS: Bin(2),Indep,Trials(til 1st),SuccP(same). X=#Trial. Calc: pdf/cdf",
            "Normal": "N(mu,s). Bell, Symm. Z=(x-mu)/s. 68-95-99.7 Rule(+/-1,2,3s). Calc: cdf(prob), invN(value)",
            "Assess Norm": "Graph(Hist,Box), NormProbPlot(Lin)"
        }
    },
    "Sampling Dists": {
        "Concepts": {
            "SampDist": "Dist of Stat from all samples.",
            "CLT": "SampDist Norm if Pop Norm OR n>=30.",
            "Mean": "mu=mu, s=s/sqrt(n). SE=s/sqrt(n)",
            "Prop (p-hat)": "mu=p, s=sqrt(pq/n). SE=sqrt(p^q^/n)",
            "Diff Means": "mu=mu1-mu2, s=sqrt(s1^2/n1+s2^2/n2). SE=sqrt(s1^2/n1+s2^2/n2)",
            "Diff Props": "mu=p1-p2, s=sqrt(p1q1/n1+p2q2/n2). SE=sqrt(p^1q^1/n1+p^2q^2/n2)"
        }
    },
    "Inference CI": {
        "Concepts": {
            "CI": "Estimate Param: Stat +/- CritVal * SE(Stat)",
            "Steps": "1.Conditions 2.Calc 3.Concl",
            "Conclude": "We are [x]% confident that the true [parameter] of [context] is between [a] and [b].",
            "ME": "MarginErr = CritVal*SE. decrease ME: decrease C%, increase n, decrease s/p^q^",
            "T-Dist": "Use if s unknown (means). df=n-1 (or calc). More spread/tails > Z."
        }
    },
    "Inference HT": {
        "Concepts": {
            "HT": "Test claim H0 vs Ha (<,>,!=)",
            "Steps": "1.Cond 2.Hyp(H0,Ha,Define Param!) 3.Calc(Stat, Pval) 4.Concl",
            "P-Value": "Prob of stat (or more extreme) IF H0 true.",
            "Decision": "Pval<alpha -> Reject H0 | Pval>=alpha -> Fail Reject H0",
            "Conclude": "Evidence(suff/insuff) for Ha [context].",
            "Errors": "Type I(Reject true H0, P=alpha), Type II(FailRej false H0, P=beta). alpha up <-> beta down",
            "Power": "P(Reject H0 | H0 False) = 1-beta. increase Power: increase alpha, increase n, increase |EffectSize|"
        }
    },
    "Chi-Square": {
        "Concepts": {
            "Use": "Counts / Cat Data. Skew R Dist.",
            "Tests": "GoF(1s,1v), Indep(1s,2v), Homog(>=2s,1v)",
            "GoF": "Obs vs Exp Fit? df=cat-1.",
            "Indep/Homog": "Exp=(Row*Col)/GrandTot. df=(r-1)(c-1).",
            "Cond": "Rand, All Exp Counts >= 5"
        }
    },
    "Reg Inference": {
        "Concepts": {
            "Model": "mu=a+bx. Slope HT/CI on b.",
            "CI b": "b +/- t* SEb (df=n-2)",
            "Test b": "H0:b=0. t = (b-0)/SEb (df=n-2)"
        }
    },
    "Conditions": {
        "Concepts": {
            "Props(Z)": "Rand; Norm(np,n(1-p)>=10); Indep(Pop>=10n). 2Samp: Both + Indep Samp.",
            "Means(T)": "Rand; Norm(PopNorm/CLT n>=30/Graph ok); Indep(Pop>=10n). 2Samp: Both + Indep Samp.",
            "Pairs(T)": "Rand Pair; Diff Norm(CLT n>=30/Graph ok); Indep Pair.",
            "chi^2": "Rand; Exp Counts >= 5.",
            "LinReg(T)": "LINER: Lin(Resid Plot), Indep Obs, Norm Resids(Hist/NPP), EqVar Resids(Resid Plot), Rand."
        }
    }
}
