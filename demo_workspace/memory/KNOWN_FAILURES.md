# Known Failures

## Demo Failure: Validation Was an Afterthought

A previous AI session produced a plausible config change but never defined how to check it. The follow-up session had to rediscover the validation command.

Prevention: every task starts with `validation_plan`.

