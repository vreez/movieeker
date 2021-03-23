<template>
  <div>
    <div class="detail-main">
      <h1 class="main-title">영화 상세 정보</h1>
    </div>
    <div class="movie-detail">
      <img :src="posterURI" alt="">
      <br>
      <br>
      <span class="movie-title">{{ $route.query.title }}</span>
      <br>
      <p class="score">{{ $route.query.vote_average }}</p>
      <br>
      <p class="overview">{{ $route.query.overview }}</p>
      <br>
      <br>
      <strong style="font-size:20px">genre</strong> 
      
        <div v-for="(genre) in genres" :key="genre.id" :genre="genre">
          {{ genre.name }}
        
        </div>
      <br>
      내 평점 : {{ this.score }}
      <b-button class="delete-btn" variant="danger" @click="deleteRank">X</b-button>
      <br>
      <br>
      <div class="star">
        <star-rating 
          v-model="rating"
          :increment="0.5"
          :max-rating="10"
          :star-size="40"
          @rating-selected="setRating"
          
        />
      </div>
    </div>
  </div>
</template>

<script src="https://unpkg.com/vue-star-rating/dist/VueStarRating.umd.min.js"></script>
<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
export default {
  name: 'DetailMovie',
  components: {
    StarRating,
  },
  data() {
    return {
      // 별점기능에 쓰일 별점 변수rating
      rating: 0,
      genres: '',

      // 내가 주는 평점 데이터
      score: 0,

      content: '',
      scoreList: [],
      contentList: [],
      show: false,
    }
  },
  computed: {
    posterURI() {
      const posterId = this.$route.query.poster_path
      return `https://image.tmdb.org/t/p/w200/${posterId}`
    },
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
  
    setRating(rating) {
      this.rating = rating
      const movieId = this.$route.query.id
      const postItem = {
        rank: this.rating
      }
      const config = this.setToken()
      axios.post(`http://127.0.0.1:8000/movies/${movieId}/`, postItem, config)
        .then(res => {
          // 내가 줄 평점
          this.score = res.data
        })
        .catch(err => {
          console.log('에러ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ')
        })
    },
    deleteRank() {
      const movieId = this.$route.query.id
      const postItem = {
        rank: 0
      }
      const config = this.setToken()
      axios.post(`http://127.0.0.1:8000/movies/${movieId}/`, postItem, config)
        .then(res => {
          // 내가 줄 평점
          this.score = res.data
        })
        .catch(err => {
          console.log('에러ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ')
        })
    }
    
  },
  created() {
    const config = this.setToken()
    const movieId= this.$route.query.id
    this.genres = this.$route.query.genres
    axios.get(`http://127.0.0.1:8000/movies/${movieId}/rank/`, config)
      .then(res => {
        console.log(res)
        // 현재 내가 준 평점
        this.score = res.data
      })
  }
}
</script>

<style scoped>

  .detail-main {
    height: 400px;
    background-image: url(https://img.extmovie.com/files/attach/images/135/724/002/052/d16b8a8ce1d1b0bdd76a26d7929563ff.gif);
    margin-bottom: 80px;
    background-size: 1920px;
    filter: grayscale(100%);
  }

  .main-title {
    color:white;
    position: relative;
    padding-top: 180px;
    font-weight: bold;
  }
  .movie-detail {
    text-align: center;
  }
  .movie-title {
    margin-top: 15px;
    font-size: 30px;
    font-weight: bold;
    color: rgb(27, 26, 26);
  }

  .score {
    font-size: 22px;
    color: rgb(216, 38, 97);
  }
  .overview {
    width: 600px;
    margin: 0 auto;
    color: black;
  }

  .star {
    width: 400px;
    margin: 0 auto;
    margin-bottom: 150px;
  }

  .delete-btn {
    margin-left: 4px;
  }
</style>