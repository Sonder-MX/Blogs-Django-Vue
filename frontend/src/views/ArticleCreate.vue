<template>
  <BlogHeader />

  <div id="article-create">
    <h3>发表文章</h3>
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
            type="button"
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
        <textarea v-model="article.body_cont" placeholder="输入正文" rows="20" cols="80"></textarea>
      </div>

      <div class="form-elem">
        <button v-on:click.prevent="submit">提交</button>
      </div>
    </form>
  </div>

  <BlogFooter />
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import BlogFooter from "@/components/BlogFooter.vue"

import { reactive, onMounted } from "vue"
import { useRouter } from "vue-router"
import { sendGetReq, sendPostReq } from "@/http"
import authorization from "@/utils/authorization"

const router = useRouter()
let article = reactive({
  title: "",
  tags: "",
  body_cont: "",
  categories: [],
  selectCategorie: null,
})

onMounted(() => {
  sendGetReq("/category/").then((resData) => {
    article.categories = resData
  })
})

function categoryStyle(catego) {
  if (article.selectCategorie !== null && catego.id === article.selectCategorie.id) {
    return { backgroundColor: "rgb(61, 179, 242)" }
  }
  return { backgroundColor: "rgb(214, 216, 219)" }
}

function chooseCategory(catego) {
  // 如果点击已选取的分类，则将 article.selectCategorie 置空
  if (article.selectCategorie !== null && article.selectCategorie.id === catego.id) {
    article.selectCategorie = null
  }
  // 如果没选中当前分类，则选中它
  else {
    article.selectCategorie = catego
  }
}

function submit() {
  authorization().then((resp) => {
    if (resp[0]) {
      // 需要传给后端的数据
      let payload = {
        title: article.title,
        body: article.body_cont,
        tags: article.tags
          .split(/[,，]/)
          .map((x) => x.trim())
          .filter((x) => x.charAt(0) !== ""), // 去除空提交
      }
      // 添加分类
      if (article.selectCategorie) {
        payload.category_id = article.selectCategorie.id
      }

      const token = localStorage.getItem("access.myblog")
      sendPostReq("/article/", payload, { headers: { Authorization: "Bearer " + token } }).then(
        (res) => {
          router.push({ name: "ArticleDetail", params: { id: res.data.id } })
        }
      )
    } else {
      alert("令牌过期，请重新登录。")
      router.push({ name: "Login" })
    }
  })
}
</script>

<style scoped>
.tmp {
  background-color: rgb(61, 179, 242);
  color: white;
}

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
  width: 75px;
}
</style>
