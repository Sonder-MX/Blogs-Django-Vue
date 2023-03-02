<template>
  <BlogHeader />

  <div id="article-create">
    <h3>更新文章</h3>
    <form>
      <div class="form-elem">
        <span>标题：</span>
        <input v-model="article.title" type="text" placeholder="输入标题" />
      </div>

      <div class="form-elem">
        <span>分类：</span>
        <span v-for="category in article.categories" :key="category.id">
          <!--样式也可以通过 :style 绑定-->
          <button
            class="category-btn"
            :style="categoryStyle(category)"
            @click.prevent="chooseCategory(category)">
            {{ category.title }}
          </button>
        </span>
      </div>

      <div class="form-elem">
        <span>标签：</span>
        <input v-model="article.tags" type="text" placeholder="输入标签，用逗号分隔" />
      </div>

      <div class="form-elem">
        <span>正文：</span>
        <textarea v-model="article.body" placeholder="输入正文" rows="20" cols="80"></textarea>
      </div>

      <div class="form-elem">
        <button v-on:click.prevent="submit">提交</button>
      </div>
      <div class="form-elem">
        <button v-on:click.prevent="deleteArticle" style="background-color: rgb(241, 148, 148)">
          删除
        </button>
      </div>
    </form>
  </div>
  <BlogFooter />
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import BlogFooter from "@/components/BlogFooter.vue"

import { reactive, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { sendGetReq, sendPutReq, sendDeleteReq } from "@/http"
import axios from "axios"
import authorization from "@/utils/authorization"

const route = useRoute()
const router = useRouter()
let article = reactive({
  title: "",
  body: "",
  categories: [],
  selectedCategory: null,
  tags: "",
  // Article id
  articleID: null,
})
onMounted(() => {
  // 页面初始化时获取所有分类
  sendGetReq("/category/").then((resp) => (article.categories = resp))
  //
  sendGetReq("/article/" + route.params.id + "/").then((resp) => {
    article.title = resp.title
    article.body = resp.body
    article.selectedCategory = resp.category
    article.tags = resp.tags.join(",")
    article.articleID = resp.id
  })
})

// 根据分类是否被选中，按钮的颜色发生变化
function categoryStyle(category) {
  if (article.selectedCategory !== null && category.id === article.selectedCategory.id) {
    return { backgroundColor: "rgb(61, 179, 242)" }
  }
  return { backgroundColor: "rgb(214, 216, 219)" }
}

// 选取分类
function chooseCategory(catego) {
  if (article.selectedCategory !== null && article.selectedCategory.id === catego.id) {
    article.selectedCategory = null
  } else {
    article.selectedCategory = catego
  }
}

function submit() {
  authorization().then((response) => {
    if (response[0]) {
      let data = {
        title: article.title,
        body: article.body,
        category_id: article.selectedCategory ? article.selectedCategory.id : null,
        tags: article.tags
          .split(/[,，]/)
          .map((x) => x.trim())
          .filter((x) => x.charAt(0) !== ""),
      }

      const token = localStorage.getItem("access.myblog")
      sendPutReq("/article/" + article.articleID + "/", data, {
        headers: { Authorization: "Bearer " + token },
      }).then((resp) => {
        router.push({ name: "ArticleDetail", params: { id: resp.data.id } })
      })
    } else {
      alert("令牌过期，请重新登录。")
      router.push({ name: "Home" })
    }
  })
}

function deleteArticle() {
  const token = localStorage.getItem("access.myblog")
  authorization().then((response) => {
    if (response[0]) {
      if (confirm("确定要删除该文章吗？")) {
        sendDeleteReq("/article/" + article.articleID + "/", {
          headers: { Authorization: "Bearer " + token },
        }).then(() => router.push({ name: "Home" }))
      }
    } else {
      alert("令牌过期，请重新登录。")
      router.push({ name: "Home" })
    }
  })
}
</script>

<style scoped>
.category-btn {
  margin-right: 10px;
}
#article-create {
  text-align: center;
  font-size: large;
}
form {
  text-align: left;
  padding-left: 100px;
  padding-right: 10px;
}

.form-elem {
  padding: 10px;
}

input {
  height: 25px;
  padding-left: 10px;
  width: 50%;
}

button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: rgb(214, 216, 219);
  color: rgb(12, 12, 12);
  border-radius: 5px;
  width: 80px;
}
</style>
