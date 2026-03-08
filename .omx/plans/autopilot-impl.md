# Autopilot Implementation Plan: Acceptance Strategy (Data/Theory-only)

## Target Journal Strategy

### Primary target (if upgraded strongly): The Lancet Public Health
- Acceptance condition (practical): move from association paper to policy-causal evidence with strong external validity and quantified fiscal impact.

### Secondary targets (high probability if full upgrade completed)
- JAMA Network Open
- The BMJ

### Field-optimized fallback (still top in domain)
- Journal of Health Economics
- Health Services Research
- Medical Care
- Value in Health

## Workstream 1: Causal Identification Upgrade
Goal: Replace simple adjusted association narrative with causal estimand-focused design.

1. Define estimands
- ATE of moving from Participation-only to Tier 3 (and Tier 2/1) on 12-month total costs.
- Age-by-sex stratified CATEs.

2. Core estimators (must all run)
- Doubly robust AIPW / TMLE with rich confounder set.
- Generalized propensity score weighting for ordinal tiers.
- Two-part cost model (Pr(cost>0) + positive-cost GLM/Tweedie) to handle zero mass explicitly.

3. Identification diagnostics
- Covariate balance (SMD < 0.10 post-weighting for all key covariates).
- Positivity diagnostics and truncation sensitivity.

## Workstream 2: Bias and Robustness Battery
Goal: top-tier-grade credibility against reverse causality/selection bias.

1. Selection bias correction
- Model linkage/inclusion probability from 660,604 -> 154,051 and apply IPW calibration.

2. Unmeasured confounding sensitivity
- E-value or Rosenbaum-style sensitivity for key contrasts.
- Negative-control outcome and/or exposure analyses.

3. Model robustness
- Compare gamma-log, Tweedie, log-normal, and quantile models.
- Report consistency of sign/magnitude across model families.

## Workstream 3: Policy Translation and Economic Theory Contribution
Goal: introduce a new, testable theory layer + policy-relevant counterfactuals.

1. Theory proposal
- Functional Reserve–Expenditure Gradient (FREG) model:
  - Hypothesis H1: below a functional threshold, expected cost gradient is convex (nonlinear increase).
  - H2: mobility/agility metrics mediate high-cost event risk more strongly in older adults.

2. Quantitative policy simulation
- Scenario S1: shift 10% of Participation-only -> Tier 3.
- Scenario S2: shift 10% -> Tier 2.
- Scenario S3: shift 10% -> Tier 1 (upper-bound).
- Output: annual and 5-year budget impact with 95% uncertainty intervals.

## Acceptance-Level Numeric Targets (must-hit)

1. Credibility targets
- Post-weighting max SMD <= 0.10.
- No sign reversal for primary contrasts across >=4 model families.
- Primary senior-group contrast CI excludes 0 in all causal estimators.

2. Predictive/transport targets
- Temporal holdout (e.g., train 2015-2019, validate 2020-2022):
  - Calibration slope 0.9-1.1
  - Relative error <=10% for aggregate cost predictions.

3. Policy utility targets
- At least one realistic shift scenario yields statistically reliable net savings (95% UI entirely below zero cost increase).
- Heterogeneity map identifies priority subgroup with >=1.5x larger marginal savings than cohort average.

## Computational Experiment Design (No physical experiment)

Experiment E1: Data QA and cohort flow reproducibility
- Reconstruct full inclusion flow and missingness matrix.
- Deliver STROBE-style transparent cohort diagram with counts and reasons.

Experiment E2: Causal tier-effect estimation
- Implement ordinal-tier propensity model + AIPW/TMLE estimators.
- Output ATE/CATE and uncertainty by age/sex/income strata.

Experiment E3: Cost-distribution stress test
- Compare two-part, Tweedie, gamma-log, quantile.
- Evaluate tail behavior (90th/95th percentile costs).

Experiment E4: Sensitivity and falsification
- Negative controls, E-value, exclusion windows for severe baseline illness.

Experiment E5: Theory tests (FREG)
- Nonlinearity tests with splines/threshold models.
- Mobility mediation decomposition for seniors.

Experiment E6: Policy counterfactual simulator
- Micro-simulation for population-level tier shifts.
- Report yearly and 5-year KRW/USD savings with bootstrap intervals.

## Manuscript Rewrite Blueprint (required for acceptance probability)
- Abstract: shift from "association" to "causal-policy inference" wording only after robustness success.
- Methods: explicit DAG, estimands, assumptions, diagnostics, sensitivity plan.
- Results: prioritize absolute savings and uncertainty over only p-values.
- Discussion: clearly separate evidence-supported claims vs policy extrapolation.

## 6-week execution cadence (suggested)
- Week 1: data audit + cohort/quality diagnostics
- Week 2-3: causal estimators + balance/positivity
- Week 4: robustness + falsification
- Week 5: policy simulation + subgroup targeting
- Week 6: manuscript rewrite + journal-specific cover letter package
