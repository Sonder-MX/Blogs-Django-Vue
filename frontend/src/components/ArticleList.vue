<template>
  <div v-for="article in info.results" v-bind:key="article.url" id="articles">
    <div>
      <span v-for="tag in article.tags" v-bind:key="tag" class="tag">
        {{ tag }}
      </span>
    </div>
    <div class="article-title">
      {{ article.title }}
    </div>
    <div>{{ formatted_time(article.created) }}</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { reqArticleList } from "../http"

let info = ref("")
onMounted(() => {
  reqArticleList("/article")
    .then((resp) => (info.value = resp))
    .catch((err) => console.log(err.message))
})

// 方法
function formatted_time(iso_date_string) {
  const date = new Date(iso_date_string)
  return date.toLocaleDateString()
}
</script>

<!-- "scoped" 使样式仅在当前组件生效 -->
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
</style>
