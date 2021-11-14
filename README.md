# AF-SL

Sök jobb med pendlingsavstånd (Tid/Avstånd) som en preferens parameter.

Search for work with commuting distance (Time/Disctance)


# Slutmålet / The end goal

Målet med repot är att öka livskvaliteten och minska miljöbelastningen genom att erbjuda möjligheten till enklare kunna välja jobb utifrån pendlingsavstånd.

```bash
search.py <jobb sök term>
```

`search.py` kräver en API nyckel från Arbetsförmedlingen och Stockholm Lokaltrafik via TrafikLab).


## Searches

### Data som behövs är:

- Jobb sök term

- Den sökandes hemma address eller annan startaddress för pendling till arbetsplats

- När ska man vara på arbetsplatsen, fast tid eller flexibel tid. Klockslag.

### Då kan följande steg tas:

1. JobSearch

Sökmotor som gör det möjligt att söka och filtrera bland alla jobbannonser på Arbetsförmedlingens annonsplattform Platsbanken. 

2. SL Nearby stops v2.0 (Närliggande hållplatser 2)

Med detta API kan du få information om närliggande hållplatser till en försedd plats baserad på lat och long.

3. SL Route-planner v3.1 (Reseplanerare 3.1)

Med detta API kan du få reseförslag från A till B inom Stockholms län med SLs trafik. I SLs reseplanerare finns även Waxholmsbolagets trafik. APIet kan användas för att beräkna reseförslag mellan valfri kombination av position och/eller stoppställe. APIet returnerar reseförslag från ”bästa matchning” av det som läggs in.

4. Webbsida som presenterar sökt jobb där man kan sortera på pendlingsavstånd i tid eller avstånd.

### API referenser

https://jobsearch.api.jobtechdev.se/

https://jobtechdev.se/sv/produkter/jobsearch

https://www.trafiklab.se/api

https://www.trafiklab.se/api/trafiklab-apis/sl/nearby-stops-2/

https://www.trafiklab.se/api/trafiklab-apis/sl/route-planner-31/

