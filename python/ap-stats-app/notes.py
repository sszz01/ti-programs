NOTES = {
    "Descriptive Data": {
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
            "LSRL": "ŷ=a+bx. Min Se^2. x(Expl) y(Resp).\n Lower s and higher r^2 -> better LSRL.",
            "Resid": "e = y-ŷ (Act-Pred). Se=0. Plot: No pattern -> Lin OK",
            "R^2": "% var y explained by LSRL(x,y)",
            "Interpret": "b: Per 1x, ŷ change by b. r: Str,Dir,Lin assoc. R^2: %var y expl.",
            "Caution": "Extrap(Bad!). Influential(above/below: shift, far: slope change). Outlier(large e)."
        }
    },
    "Data Collection": {
        "Concepts": {
            "Samp Meth": "SRS, Strat(Grp->SRS), Clust(Loc->All), Syst(kth)",
            "Bias": "Vol, Conv, UnderCov, NonResp, Resp, Wording",
            "Study": "Obs(watch) vs Exp(treat)",
            "Exp Design": "Units, Factor(ExplVar), Level, RespVar, Treatmt",
            "Exp Princ": "Control(const), Replicate(many), Randomize(assign), Comparison",
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
            "Binomial": "BINS: Succ/Fail,Indep,N(fix#),SuccP(same). X=#Succ. Calc: pdf(P(X=x)), cdf(P(X<=x))\n1 - binomialcdf(n, p, (x -1)) = cumulative outcome P(X >= x)",
            "Geometric": "BITS: Succ/Fail,Indep,Trials(til 1st),SuccP(same). X=#Trial. Calc: pdf/cdf",
            "Normal": "N(mu,s). Bell, Symm. Z=(x-mu)/s. 68-95-99.7 Rule(+/-1,2,3s). Calc: cdf(prob), invN(value)",
            "Assess Norm": "Graph(Hist,Box), NormProbPlot(Lin)"
        }
    },
    "Sampling Distributions": {
        "Concepts": {
            "SampDist": "Dist of Stat from all samples.",
            "CLT": "SampDist Norm if Pop Norm OR n>=30.",
            "Mean": "mu=mu, s=s/sqrt(n). SE=s/sqrt(n)",
            "Prop (p-hat)": "mu=p, s=sqrt(pq/n). SE=sqrt(p^q^/n)",
            "Diff Means": "mu=mu1-mu2, s=sqrt(s1^2/n1+s2^2/n2). SE=sqrt(s1^2/n1+s2^2/n2)",
            "Diff Props": "mu=p1-p2, s=sqrt(p1q1/n1+p2q2/n2). SE=sqrt(p^1q^1/n1+p^2q^2/n2)",
            "Changes": "Increasing sample size = variability decreases."
        }
    },
    "Inference CI": {
        "Concepts": {
            "CI": "Estimate Param: Stat +/- CritVal * SE(Stat)",
            "Steps": "1.Params 2.Conditions(IF BOTH REPEAT FOR ALL) 3.Calc 4.Conclude",
            "Conclude CI": "We are [x]% confident that the interval from [a] and [b] captures the true [parameter] of [context].",
            "Conclude CL": "If we take many, many samples, we can expect about [x]% of them to capture the true [parameter] of [context].",
            "ME": "MarginErr = CritVal*SE. inc/dec ME: inc/dec C%; inc/dec n, dec/inc ME, BIAS=NO ME CHANGE",
            "T-Dist": "Use if s unknown (means). df=n-1 (or calc). More spread/tails > Z. \nApprox. normal if: Pop=Normal, n>=30(CLT), no skwness/outliers.",
        }
    },
    "Inference HT": {
        "Concepts": {
            "HT": "Test claim H0 vs Ha (<,>,!=)",
            "Steps": "1.Hyp(H0,Ha,Define Param!) 2.Cond(IF BOTH REPEAT FOR ALL) 3.Calc(Stat, Pval) 4.Concl",
            "P-Value": "Prob of stat (or more extreme) IF H0 true.",
            "Decision": "Pval<alpha -> Reject H0 | Pval>=alpha -> Fail Reject H0",
            "Conclude": "Reject/Fail Reject H0. We have (suff/insuff) evidence that the true [parameter+context].",
            "Errors": "Type I(Reject true H0, P=alpha), Type II(FailRej false H0, P=beta). alpha up <-> beta down",
            "Power": "P(Reject H0 | H0 False) = 1-beta. increase Power: increase alpha, increase n, increase |dist between H0 and Ha|"
        }
    },
    "Chi-Square": {
        "Concepts": {
            "Use": "Counts / Cat Data. Skew R Dist.",
            "Tests": "GoF(1s,1v), Indep(1s,2v), Homog(>=2s,1v)",
            "GoF": "Obs vs Exp Fit? df=cat-1.",
            "Indep/Homog": "Exp=(Row*Col)/GrandTot. df=(r-1)(c-1).",
            "Result": "Higher test-stat -> more deviation from exp."
        }
    },
    "Reg Inference": {
        "Concepts": {
            "Model": "mu=a+bx. Slope HT/CI on b.",
            "CI b": "b +/- t* SEb (df=n-2)",
            "Test b": "H0:b=0. t = (b-0 (null val) )/SEb (df=n-2)",
            "Bounds": "b<0: t-val upper. b>0: t-val lower. b!=0 consider both sides of t-val and double p-val.",
        }
    },
    "Conditions": {
        "Concepts": {
            "Props(Z)": "Rand; Norm(np,n(1-p)>=10); Indep(Pop<=0.1N). 2Samp: Both + Indep Samp.",
            "Means(T)": "Rand; Norm(PopNorm/CLT n>=30/Graph ok); Indep(Pop<=0.1N). 2Samp: Both + Indep Samp.",
            "Pairs(T)": "Rand Pair; Diff Norm(CLT n>=30/Graph ok); Indep Pair.",
            "chi^2": "Rand; Exp Counts >= 5.",
            "LinReg(T)": "LINER: Lin(Resid Plot), Indep Obs(Exp), Norm(No outlrs/skwnss), EqVar Resids(Resid Plot), Rand."
        }
    }
}
