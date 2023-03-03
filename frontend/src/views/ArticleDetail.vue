<template>
  <BlogHeader />

  <div v-if="art.article !== null" class="grid-container">
    <div>
      <h1 id="title">{{ art.article.title }}</h1>
      <p id="subtitle">
        本文由 {{ art.article.author.username }} 发布于 {{ formatted_time(art.article.created) }}
        <span v-show="isSuperUser">
          <router-link :to="{ name: 'ArticleEdit', params: { id: art.article.id } }">
            更新与删除
          </router-link>
        </span>
      </p>
      <div v-html="art.article.body_html" class="article-body"></div>
    </div>
    <div>
      <h3>目录</h3>
      <div v-html="art.article.toc_html" class="toc"></div>
    </div>
  </div>

  <Comments :article="art.article" />

  <BlogFooter />
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import Comments from "@/components/Comments.vue"
import BlogFooter from "@/components/BlogFooter.vue"

import { sendGetReq } from "@/http"
import axios from "axios"
import { onMounted, computed, reactive, onBeforeMount } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
let art = reactive({
  article: null,
})

onMounted(() => {
  sendGetReq("/article/" + route.params.id)
    .then((resp) => (art.article = resp))
    .catch((err) => console.log(err.message))
})

const isSuperUser = computed(() => {
  return localStorage.getItem("isSuperuser.myblog") === "true"
})

const formatted_time = (iso_date_string) => {
  const date = new Date(iso_date_string)
  return date.toLocaleDateString()
}
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: 3fr 1fr;
}

#title {
  text-align: center;
  font-size: x-large;
}

#subtitle {
  text-align: center;
  color: gray;
  font-size: small;
}
</style>

<style>
.article-body p img {
  max-width: 100%;
  border-radius: 50px;
  box-shadow: gray 0 0 20px;
}

.toc ul {
  list-style-type: none;
}

.toc a {
  color: gray;
}
</style>
