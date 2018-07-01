# Greenhub

## Description

Make your Github contribution graph green by adding dump commits and changing committing dates.

## Demo

A demo account is [senhungw](https://github.com/senhungw).

## How to use

1. Download the scripts

```bash
$ git clone https://github.com/senhungwong/greenhub.git
```

2. Put the downloaded files into your repository

3. Run command (see more [Commands](#commands))

## Commands

### Everyday

Commit everyday from a given date til now

```bash
$ python3 green everyday
```

```
Params:

--start_date              : the start date of the commit, default 380 days ago
--commit_times_lower_bound: the everyday commit times lower bound, default 1
--commit_times_upper_bound: the everyday commit times upper bound, default 1
--push                    : push the commits at the end
--force                   : do a force push if is pushing
```

If you set a lower bound or upper bound, on each date, it will generate a random number between the bounds and commit
that number of times.
