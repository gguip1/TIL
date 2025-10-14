data class Album(val year:Int, val title:String)

fun main(args: Array<String>){
    val Q = readLine()!!.toInt()
    
    val albums: MutableList<Album> = mutableListOf<Album>()
    albums.add(Album(1967, "DavidBowie"))
    albums.add(Album(1969, "SpaceOddity"))
    albums.add(Album(1970, "TheManWhoSoldTheWorld"))
    albums.add(Album(1971, "HunkyDory"))
    albums.add(Album(1972, "TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars"))
    albums.add(Album(1973, "AladdinSane"))
    albums.add(Album(1973, "PinUps"))
    albums.add(Album(1974, "DiamondDogs"))
    albums.add(Album(1975, "YoungAmericans"))
    albums.add(Album(1976, "StationToStation"))
    albums.add(Album(1977, "Low"))
    albums.add(Album(1977, "Heroes"))
    albums.add(Album(1979, "Lodger"))
    albums.add(Album(1980, "ScaryMonstersAndSuperCreeps"))
    albums.add(Album(1983, "LetsDance"))
    albums.add(Album(1984, "Tonight"))
    albums.add(Album(1987, "NeverLetMeDown"))
    albums.add(Album(1993, "BlackTieWhiteNoise"))
    albums.add(Album(1995, "1.Outside"))
    albums.add(Album(1997, "Earthling"))
    albums.add(Album(1999, "Hours"))
    albums.add(Album(2002, "Heathen"))
    albums.add(Album(2003, "Reality"))
    albums.add(Album(2013, "TheNextDay"))
    albums.add(Album(2016, "BlackStar"))

    for (i in 0 until Q){
        val (S, E) = readLine()!!.split(" ").map {it.toInt()}
        val filtered = albums.filter{ it.year in S..E }
        
        println(filtered.size)
        for (album in filtered){
            println("${album.year} ${album.title}")
        }
    }
}