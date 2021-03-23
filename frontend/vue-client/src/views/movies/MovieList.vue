<template>
  <div>
    <div class="main">
      <h1 class="main-title" style="font-weight:bold">MovieList</h1>
    </div>
    <div class="nowplaying">
      <div class="genre">
        <h3 style="font-weight:bold">Now Playing Movies🎬</h3>
      </div>
      <div class="nowplaying-movie">
        <ListNowPlaying
          v-for="(movie, idx) in nowplayingmovies"
          :key="idx"
          :movie="movie"
        />
        <br>
      </div>
    </div>
    <div class="popular">
      <div class="genre">
        <h3 style="font-weight:bold">Popular Movies🎬</h3>
      </div>
      <div class="popular-movie">
        <ListPopular
          v-for="(movie, idx) in popularmovies"
          :key="idx"
          :movie="movie"
        />
        <br>
      </div>
    </div>
    <div class="high-rating">  
      <div class="genre">
        <h3 style="font-weight:bold">High Rating Movies🎬</h3>
      </div>
      <div class="high-rating-movie">
        <ListVoteAverage
          v-for="(movie, idx) in voteaveragemovies"
          :key="idx"
          :movie="movie"
        />
        <br>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ListNowPlaying from '@/components/ListNowPlaying'
import ListPopular from '@/components/ListPopular'
import ListVoteAverage from '@/components/ListVoteAverage'

export default {
  name: 'MovieList',
  components: {
    ListNowPlaying,
    ListPopular,
    ListVoteAverage,
  },
  data () {
    return {
      nowplayingmovies: '',
      popularmovies: '',
      voteaveragemovies: '',
      rating: 0,
    }
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getNowPlayingMovies() {
      const config = this.setToken()
      axios.get('http://127.0.0.1:8000/movies/nowplaying/', config)
      .then(res => {
        console.log(res.data)
        this.nowplayingmovies = res.data
      })
      .catch(err => {
        console.log(err)
        console.log('실패')
      })
    },
    getPopularMovies() {
      const config = this.setToken()
      axios.get('http://127.0.0.1:8000/movies/popular/', config)
      .then(res => {
        console.log(res.data)
        this.popularmovies = res.data
      })
      .catch(err => {
        console.log(err)
        console.log('실패')
      })
    },
    getVoteAverageMovies() {
      const config = this.setToken()
      axios.get('http://127.0.0.1:8000/movies/voteaverage/', config)
      .then(res => {
        console.log(res.data)
        this.voteaveragemovies = res.data
      })
      .catch(err => {
        console.log(err)
        console.log('실패')
      })
    }
  },
  created() {
    this.getNowPlayingMovies()
    this.getPopularMovies()
    this.getVoteAverageMovies()
  }
}
</script>

<style scoped>
  .main {
    height: 400px;
    background-image: url(https://c.tenor.com/EXDsaGxikqcAAAAd/her-movie-her-movie-gif.gif);
    margin-bottom: 20px;
    background-size: 1920px;
    filter: grayscale(100%);
  }

  .main-title {
    color:white;
    position: relative;
    padding-top: 180px;
    font-weight: bold;
  }

  .genre {
    margin-top: 100px;
    margin-bottom: 80px;
  }
  .nowplaying {
    margin-bottom: 100px;
    display: inline;
  }

  .nowplaying-movie {
    margin: 0 auto;
    width: 90%;
    overflow: hidden;
    padding-left: 5%;
  }

  .popular {
    margin-bottom: 100px;
    display: inline;
  }

  .popular-movie {
    margin: 0 auto;
    width: 90%;
    overflow: hidden;
    padding-left: 5%;
  }

  .high-rating {
    margin-bottom: 100px;
    display: inline;
  }

  .high-rating-movie {
    margin: 0 auto;
    width: 90%;
    overflow: hidden;
    padding-left: 5%;
  }

</style>