<template>
  <div>
    <div class="movies">
      <div class="movie-des" @click="getMovieId">
        <div>
          <img :src="posterURI" alt="">
        </div>
        <div>
          <span class="title">{{ movie.title }}</span>
          <p>{{ movie.vote_average }}</p>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import axios from 'axios'

export default {
  name: 'ListPopular',
  props: {
    movie: Object
  },
 
  data () {
    return {
      selectedMovie: '',
    }
  },
  computed: {
    posterURI() {
      const posterId = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w200/${posterId}`
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
    getMovieId() {
      const config = this.setToken()
      const movieId = this.movie.movie_id
    
      axios.get(`http://127.0.0.1:8000/movies/${movieId}`, config)
        .then(res => {
          this.selectedMovie = res.data
          console.log(res.data)
          if (this.$router.push({ name: 'DetailMovie'}) !=='/detail' )
            this.$router.replace({ name: 'DetailMovie', query: this.selectedMovie})
        })
    }
  }
}
</script>

<style scoped>
  .movie-des {
    width: 100%;
    font-size: 20px;
    font-weight: bold;
    color: black;
    float: left;
    text-align: center;
    vertical-align: middle;
    margin-bottom: 50px;
    position: relative;
    height: 400px;
    width: 350px;
  }

  .date {
    font-size: 15px;
    color: black;
  }

  img {
    width: 200px;
    height: 300px;
    border-radius: 5%;
    z-index: 100;
    margin-bottom: 10px;
  }

  img:hover {
    filter: brightness(20%);
    cursor: pointer;
  }

</style>