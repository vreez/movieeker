<template>
  <div>
    <div class=detail-main>
      <h1 class="main-title">
        게시글 상세내용
      </h1>
    </div>
    <hr class="line">
    <div class="total-contents">
      <div>
        <label for="title"><strong>작성자</strong> | </label>
        {{ this.$route.query.user }} 
      </div>
      <div>
        <label for="title"><strong>게시일자</strong> | </label>
        {{ this.$route.query.created_at | moment('YYYY-MM-DD h:mm:ss a')}}
      </div>
      <div>
        <label for="title"><strong>수정일자</strong> | </label>
        {{ this.$route.query.updated_at | moment('YYYY-MM-DD h:mm:ss a')}} 
      </div>
      <div>
        <label for="title"><strong>제목</strong> | </label>
        <b>&emsp;{{ this.$route.query.title }}</b>
      </div>
      <div class="content-total">
        <label for="content"><strong>내용</strong>  </label>
        <h6>{{ this.$route.query.content }}</h6>
      </div>
    </div>
    
    <div class="buttons">
      <b-button variant="primary"><a href="javascript:;" @click="goToList" class="btn" style="color:white">목록</a></b-button>
      <b-button variant="danger"><a href="javascript:;" @click="checkDelete" class="btn" style="color:white">삭제</a></b-button>
      <b-button variant="outline-primary"><a href="javascript:;" @click="updatePost" class="btn">수정</a></b-button>
    </div>
    <hr class="line">
    <div>
      <h4 style="font-weight:bold">comment ({{comments.length }}개)</h4>
      <br>
      <div>
        <ul v-for="(comment, idx) in comments" :key="idx">
          <li>
            <strong>🙍🏻‍♂️{{ comment.user }}</strong>  - {{ comment.content }} | {{ comment.created_at | moment('YYYY-MM-DD h:mm:ss a')}}
            <b-button variant="outline-danger" @click="checkDeleteComment(comment)">X</b-button>
          </li>
        </ul>
      </div>
      <div class="commentbox">
        <ul>
      </ul>
        <div>
          <input class="comment-input-box" type="text" v-model.trim="content" @keypress.enter="createComment">
          <b-button variant="outline-primary" @click="createComment">댓글작성</b-button>
        </div>
      
      </div>
    </div>
  </div>

</template>

// <script>
import axios from 'axios'

export default {
  name: 'Detail',
 
  data: function () {
    const index = this.$route.query.id
    const posts = this.$route.query
    return {
      id: index,
      posts: posts,
      content: '',
      comments: '',
      commentId: Number,
}
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getComment() {
      const config = this.setToken()
      axios.get(`http://127.0.0.1:8000/community/${this.id}/comments/`, config)
        .then(res => {
          console.log('getcomment입니다')
          console.log(res)
          this.comments = res.data
        })

    },
    createComment: function () {
      const config = this.setToken()
      
      const commentItem = {
        content: this.content,
      }

      if (commentItem.content) {
        axios.post(`http://127.0.0.1:8000/community/${this.id}/comments/`, commentItem, config)
          .then((res) => {
            console.log(res)
          
            this.content = ''
            this.getComment()
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },

    deleteComment: function (comment) {
      const config = this.setToken()
      const commentId = comment.id
      const reviewId = Number(this.id)
      console.log('delete요청')
      console.log(reviewId)
      console.log(commentId)
      
      axios.delete(`http://127.0.0.1:8000/community/${reviewId}/comments/delete/${commentId}/`, config)
        .then(() => {
          this.getComment()
        })
        .catch((err) => {
          console.log('comment delete 에러')
          console.log(err)
          alert('본인 글이 아닙니다')
        })
    },
    
    goToList(){ //게시글 확인 페이지로 이동
			this.$router.push({path:'/PostList/', query:this.body});
    },

    updatePost: function () {
  
      const config = this.setToken()
      const postContent = this.$route.query
      console.log('여기는..?')
    
      axios.put(`http://127.0.0.1:8000/community/${this.$route.query.id}/`, postContent, config)
        .then(() => {
          console.log('들어왔나요?')
          console.log(postContent)
          this.$router.push({path:`/community/create/${this.$route.query.id}/`,query:postContent, params:postContent.id});
        })
        .catch((err) => {
          console.log(err)
          alert('작성자 본인만 수정할 수 있어요😉')
        })
      },

    deletePost: function () {
      const config = this.setToken()
      console.log('여기까지는?')
      axios.delete(`http://127.0.0.1:8000/community/${this.$route.query.id}/`, config)
        .then((res) => {
          this.goToList();
          console.log(res)
          console.log('삭제가 되는건가?')
          console.log(this.index)
          alert("삭제되었습니다.");
        })
        .catch((err) => {
          console.log(err)
          alert("본인 글이 아닙니다")
        })
    },
    checkDelete() {
      if (confirm('정말 삭제하시겠습니까?🤷‍♂️') == true){    //확인
        this.deletePost()
      } else {   //취소
        document.form.submit(); 
      }
    },
    checkDeleteComment(comment){
      if (confirm('정말 삭제하시겠습니까?🤷‍♂️') == true) {    //확인
        this.deleteComment(comment)
      } else {   //취소
        document.form.submit(); 
      }
    }
  
  },
  
  created() {
    this.getComment() 
    
  },
  
}
</script>
<style scoped>

  ul {
    list-style: none;
  }
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

  .total-contents {
    width: 500px;
    margin: 0 auto;
    text-align: justify;
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
    margin-bottom: 40px;
  }

  .commentbox {
    margin-bottom: 180px;
    margin-top: 40px;
  }

  .comment-input-box {
    margin-right: 3px;
    width: 350px;
    height: 37px;
  }

  .detail-main {
    height: 400px;
    background-image: url(https://extmovie.com/files/attach/images/135/864/625/039/d45f2adb0da9e2490177d26540c2c83d.gif);
    margin-bottom: 20px;
    background-size: cover;
    filter: grayscale(100%);
  }

  .main-title {
    color:white;
    position: relative;
    padding-top: 180px;
    font-weight: bold;
  }
  
  strong {
    color: rgb(38, 95, 202);
  }
  .loading span {
    display: inline-block;
    margin: 0 -.075em;
    animation: loading .7s infinite alternate;
  }
  .loading span:nth-child(2) {
    animation-delay: .1s;
  }
  .loading span:nth-child(3) {
    animation-delay: .2s;
  }
  .loading span:nth-child(4) {
    animation-delay: .3s;
  }
  .loading span:nth-child(5) {
    animation-delay: .4s;
  }
  .loading span:nth-child(6) {
    animation-delay: .5s;
  }
  .loading span:nth-child(7) {
    animation-delay: .6s;
  }
  @keyframes loading {
    0% {
      transform: scale(1);
    }
    100% {
      transform: scale(0.8);
    }
  }
</style>