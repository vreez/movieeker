<template>
  <div>
    <div @click="getMovieId">
      <div class="random">
        <h3 class="random-title">고민하는 당신을 위한 RANDOM 추천 영화😎</h3>
        <img :src="posterURI" alt="이미지가 없습니다">
        <p class="random-movie-title">{{ movie.title }}</p>
        <p class="random-date">개봉일 : {{ movie.release_date }}</p>  
        <p class="random-score">{{ movie.vote_average }}</p>
      </div>
      <hr>
    </div>
    <div>
       
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RecommendRandom',
  data() {
    return {
      selectedMovie: '',
      isMovie: false,
    }
  },
  props: {
    movie: [Object, Array],

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
    
  },
  computed: {
    posterURI() {
      console.log(this.movie)
      if (this.movie) {
        const posterId = this.movie.poster_path
        return `https://image.tmdb.org/t/p/w200/${posterId}`
      } else {
        return null
      }
    }
  },
  created() {
    
  }

  
}
</script>

<style scoped>
.random {
  margin-top: 20px;
}

.random-title {
  font-weight: bold;
  margin-top: 50px;
  margin-bottom: 30px;
}

.random-movie-title {
  color: black;
  font-weight: bold;
  font-size: 30px;
  margin-top: 15px;
}

.random-date {
  color: black;
  font-size: 18px;
}

.random-score {
  font-weight: bold;
  font-size: 27px;
}
</style>