<template>
  <div id="articles" v-for="article in articleInfo.data.results" :key="article.url">
    <div class="grid" :style="gridStyle(article)">
      <div class="image-container">
        <img :src="imageIfExists(article)" alt="" class="image" />
      </div>
      <div>
        <div class="cate-tag">
          <span v-if="article.category !== null" class="category">
            {{ article.category.title }}
          </span>
          <span class="tag" v-for="tag in article.tags" :key="tag">
            {{ tag }}
          </span>
        </div>
        <router-link
          :to="{ name: 'ArticleDetail', params: { id: article.id } }"
          class="article-title">
          {{ article.title }}
        </router-link>
        <div>{{ formatted_time(article.created) }}</div>
      </div>
    </div>
  </div>

  <div id="paginator">
    <span v-show="is_page_exists('previous')">
      <router-link :to="get_path('previous')"> Prev </router-link>
    </span>
    <span class="current-page">
      {{ get_page_param("current") }}
    </span>
    <span v-show="is_page_exists('next')">
      <router-link :to="get_path('next')"> Next </router-link>
    </span>
  </div>
</template>

<script setup>
import { onMounted, reactive, watch } from "vue"
import { useRoute } from "vue-router"
import { sendGetReq } from "@/http"

const route = useRoute()
let articleInfo = reactive({
  data: {},
})

onMounted(() => get_article_data())

// 方法
// 获取文章列表数据
function get_article_data() {
  let url = "/article"
  let params = new URLSearchParams()
  // appendIfExists 方法是原生没有的
  // 原生只有 append 方法，但此方法不能判断值是否存在
  params.appendIfExists("page", route.query.page)
  params.appendIfExists("title", route.query.title)

  const paramsString = params.toString()
  if (paramsString.charAt(0) !== "") {
    url += "/?" + paramsString
  }
  sendGetReq(url)
    .then((resp) => {
      articleInfo.data = resp
    })
    .catch((err) => console.log(err.message))
}

function formatted_time(iso_date_string) {
  const date = new Date(iso_date_string)
  return date.toLocaleDateString()
}

// 判断页面是否存在
function is_page_exists(direction) {
  return direction === "next" ? articleInfo.data.next !== null : articleInfo.data.previous !== null
}

// // 获取页码
function get_page_param(direction) {
  try {
    let url_string
    switch (direction) {
      case "next":
        url_string = articleInfo.data.next
        break
      case "previous":
        url_string = articleInfo.data.previous
        break
      default:
        // 如果page不存在或为空
        if (!("page" in route.query) || route.query.page === null) return 1
        return route.query.page
    }
    if (url_string) {
      const url = new URL(url_string)
      return url.searchParams.get("page")
    }
  } catch (err) {
    console.log(err)
  }
}

function get_path(direction) {
  let url = ""
  try {
    switch (direction) {
      case "next":
        if (articleInfo.data.next !== undefined) {
          url += new URL(articleInfo.data.next).search
        }
        break
      case "previous":
        if (articleInfo.data.previous !== undefined) {
          url += new URL(articleInfo.data.previous).search
        }
        break
    }
  } catch {
    return url
  }
  return url
}

function imageIfExists(article) {
  if (article.avatar) {
    return article.avatar.content
  }
}

function gridStyle(article) {
  if (article.avatar) {
    return {
      display: "grid",
      gridTemplateColumns: "0.2fr 4fr",
    }
  }
}

// 监听
watch(route, () => get_article_data())
</script>

<style scoped>
#articles {
  padding: 10px;
}

.article-title {
  font-size: large;
  font-weight: bolder;
  color: black;
  text-decoration: none;
  padding: 5px 0 5px 0;
}

.tag {
  padding: 2px 5px 2px 5px;
  margin: 5px 5px 5px 0;
  font-family: Georgia, Arial, sans-serif;
  font-size: small;
  background-color: #4e4e4e;
  color: whitesmoke;
  border-radius: 5px;
}

.category {
  padding: 5px 10px 5px 10px;
  margin: 5px 5px 5px 0;
  font-family: Georgia, Arial, sans-serif;
  font-size: small;
  background-color: rgb(40, 30, 77);
  color: whitesmoke;
  border-radius: 15px;
}

.cate-tag {
  padding: 8px 0;
}

#paginator {
  text-align: center;
  padding-top: 50px;
}

a {
  color: black;
}

.current-page {
  font-size: x-large;
  font-weight: bold;
  padding-left: 10px;
  padding-right: 10px;
}

.image {
  width: 180px;
  border-radius: 10px;
  box-shadow: darkslategrey 0 0 12px;
}

.image-container {
  width: 200px;
}

.grid {
  padding-bottom: 10px;
}
</style>
