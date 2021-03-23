<template>
  <div>
    <div class="movie-list">
      <NowPlaying 
      v-for="(movie, idx) in movies"
      :key="idx"
      :movie="movie"
    />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import NowPlaying from '@/components/NowPlaying'
export default {
  name: 'HomeMovie',
  components: {
    NowPlaying,
  },
  data () {
    return {
      movies: '',
      movie_id: '',
      title: '',
      poster_path: '',
      vote_average: '',
    }
  },
  methods: {
    getNowPlayingMovies() {
      axios.get('http://127.0.0.1:8000/movies/')
      .then(res => {
        // console.log(res.data)
        this.movies = res.data

      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created() {
    this.getNowPlayingMovies()
  }
}
</script>

<style>
.movie-list {
  float: left;
  margin-bottom: 300px;
  width: 100%;
  text-align: center;
  left: 50%;
  vertical-align: middle;
  margin-left: 60px;
}
</style>