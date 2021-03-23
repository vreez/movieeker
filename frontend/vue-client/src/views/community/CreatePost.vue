<template>
<div>
  <div class="main">
      <h1 class="main-title">게시글 {{index !== undefined ? '수정' : '쓰기'}}</h1>
    </div>
  <hr class="line">
  <label class="title-label" for="title"><strong>제목</strong></label>
  <input class="title" type="text" v-model.trim="title" value="title" ref="title" @keypress.enter="createPost">
  <div class="content-total">
    <label class= "content-label" for="content"><strong>내용</strong></label>
    <textarea class="content" v-model.trim="content" ref="content" name="" id="" cols="50" rows="10" value="content"></textarea>
  </div>
  <div class="buttons">
    <b-button variant="primary"><a href="javascript:;" @click="goToList" class="btn" style="color:white">목록</a></b-button>
    <b-button variant="outline-primary"><a href="javascript:;" @click="index !== undefined ? updatePost() : createPost()" class="btn">{{index !== undefined ? '수정' : '작성'}}</a></b-button>
	</div>
    <div>
  </div>
</div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreatePost',
  data: function () {
    const index = this.$route.params.id;
    return {
      index: index,
      title: index !== undefined ? this.$route.query.title : '',
      content: index !== undefined ? this.$route.query.content : '',
      user_id: '',
      created_at: '',
      updated_at: '',
      id: this.$route.query.id,
    }
  },
  methods: {
  
    goToList(){ //게시글 확인 페이지로 이동
			this.$router.push({path:'/PostList/',query:this.body});
    },
   
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    createPost: function () {
      const config = this.setToken()
      
      const postItem = {
        content_id : this.id,
        title: this.title,
        content: this.content,
        user_id: this.user_id,
        created_at: this.created_at,
        updated_at: this.updated_at,
      }

      if (postItem.title) {
        axios.post('http://127.0.0.1:8000/community/', postItem, config)
          .then((res) => {
            console.log(res.data)
            console.log(postItem)
            console.log('포스트 생성')
            this.$router.push({ name: 'PostList' })
            alert("포스트 작성이 완료되었습니다🙌")
          })
          .catch((err) => {
            console.log(12345345356)
            console.log(err)
            console.log('오류')
          })
        }
    },
    updatePost() {
      const index = this.$route.params.id;
      const config = this.setToken()

      console.log(index)
      console.log(this.$route.query)
      console.log('여기까지는 왔을까?')
     
      this.$route.query.title = this.title
      this.$route.query.content = this.content
      const postContent = this.$route.query

      axios.put(`http://127.0.0.1:8000/community/${this.$route.query.id}/`, postContent, config)
        .then(() => {
          console.log('들어왔나요?')
          console.log(postContent)
          this.$router.push({path:`/community/create/${this.$route.query.id}/`,query:postContent, params:postContent.id});
          alert('게시글 수정이 완료되었습니다!')
          this.$router.push({name: 'PostList'})
        })
        .catch((err) => {
          console.log(err)
        })
   
      console.log('쿼리수정??')
      console.log(this.$route.query)
    }
  }
}
</script>
<style scoped>

  .line {
    width: 60%;
    margin-bottom: 25px;
  }
  .title {
    width: 45%;
    margin-bottom: 10px;
  }

  .title-label {
    margin-right: 30px;
  }

  .content {
    width: 45%;
  }

  .content-label {
    margin-right: 30px;
    height: 200px;
    display: inline;
  }

  .content-total {
    vertical-align: middle;
    margin-bottom: 30px;
  }

  .btn {
    margin-right: 5px;
  }

  .buttons {
    margin-bottom: 180px;
  }

  .main {
    height: 400px;
    background-image: url(https://media1.giphy.com/media/1BGg1d0lNb1LStbfNb/source.gif);
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
</style>