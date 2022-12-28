# finn_api

Interface to API used by "finn.no".

> **DISCLAIMER:** This is only an experiment in reverse engineering and using this code could breach [finn.no's terms and conditions](https://www.finn.no/api/terms) and be against their policies for use of robots, scrapers and spiders, described [here in chapter 7](https://payment.schibsted.no/terms?client_id=5087dc1b421c7a0b79000000&locale=nb_NO). I take no responsibility for any consequences that arise from misuse of the code. The code is provided purely for educational purposes. Be responsible :)
> **WARNING:** As this is an experiment, there are no guarantees that the interface stays functional, furthermore i won't actively keep the repository up to date in case of something breaking. Use at own risk.

## TODO

- Higher level abstraction for API interface
- Automatic swiping of pages
- Build complete sitemap

## The API interface

Target endpoints:
- https://www.finn.no/realestate
    - /homes
    - /newbuildings
    - /plots
    - /leisuresale
    - /leisureplots
    - /lettings
    - /businessale
    - /businessrent
    - /businessplots
    - /companyforsale
    - /abroad
- https://www.finn.no/reise
    - /feriehus-hytteutleie
- https://www.finn.no/bap
    - /forsale
    - ++ categories
- https://www.finn.no/car
    - /used
    - /import
    - /mobilehome
    - /caravan
- https://www.finn.no/boat
    - /forsale
    - /wanted
    - /rent
    - /motor
    - /dock/available
- https://www.finn.no/mc
    - /all
    - /scooter
    - /snowmobile
    - /atv
- https://www.finn.no/b2b
    - /vanused
    - /truck
    - /bus
    - /construction
    - /agriculturetractor
    - /agriculturecombines
    - /agriculturetools
- https://www.finn.no/job
    - /fulltime
    - /management
    - /employer/companies
    - ++ occupations
- https://www.finn.no/notifications

- https://www.finn.no/innfinn/

- https://kart.finn.no/
    - https://kart.finn.no/map/api/geo/query/solr.json?type=GAB%2CPLACE&limit=5&q=oslo

- https://profil.nabolag.no/

## Endpoints of interest

- https://assets.finn.no
- https://static.finncdn.no
- https://www.finn.no/innfinn/static/images/400.jpg - -and fuzzy related
- https://www.finn.no/broadcasts
- https://dev.kart.finn.no/ -- login prompt
- https://finnno.d3.sc.omtrdc.net/
- https://finn.boost.ai/
- https://finn.boost.ai/api -- chatbot api? https://my-va.boost.ai/api
- https://cis.schibsted.com/
- wss://www.finn.no
- https://www.finn.no/innfinn/adselection/ad -- post request to create ad? redirected to https://www.finn.no/innfinn/adselection/ad/285365681. POST data is "adType: bap" and "__csrf_token: ..."
- https://cis.schibsted.com/api/v1/identify
- https://www.finn.no/innfinn/adselection/bap/update/285365681 -- updating ads possibly? POST
- https://www.finn.no/podium-resource/recommendations/haslegalbasis -- more api stuff
- https://www.finn.no/podium-resource/tjtFeed/api/transactionFeed -- more api stuff
- https://www.finn.no/podium-resource/recommendations/match-ad/recommend/frontpage-personal?rows=200&render=6&pos=m-frontpage_v2ads -- front-page recommendations
- https://www.finn.no/ec/ -- event collector
- https://www.finn.no/auth
- https://images.finncdn.no

## Notes

Found: "api='https://www.finn.no/broadcasts'" in source. Pinging current path every minute.

User related endpoint: https://www.finn.no/header-proxy/podium-resource/header/api

https://www.finn.no/csp-report.html?app_name=innfinn, GET method not allowed

https://sdk.pulse.schibsted.com/ -- schibsted pulse api

https://cdnjs.cloudflare.com/

sb.scorecardresearch.com -- shady ish

"this.isDev ? (this.providerId = "finndev" " -- found in "finn-pulse-init.min.js"

Tracker json scheme: http://schema.schibsted.com/events/tracker-event.json/331.json

https://collector.schibsted.io/api/v1/track -- trackers

Found: `score":0.7752794"`, `"published_relative":"3 dager siden"`, in https://www.finn.no/podium-resource/recommendations/match-ad/recommend/frontpage-personal?rows=200&render=6&pos=m-frontpage_v2ads -- ad matching score

https://www.finn.no/auth/refresh?hash=d670df97585330870accfb88b544c9188de118a4248094ea80ccdea5d4671684 -- hash refresh of some sort?

https://www.finn.no/podium-resource/login-refresh/track -- tracker creation, POST

https://www.finn.no/clientstats.html -- clientstats, POST

Could be interesting: https://hjelpesenter.finn.no/hc/no/articles/303324-Tips-om-friteksts%C3%B8k-og-ord-i-annonsen-
