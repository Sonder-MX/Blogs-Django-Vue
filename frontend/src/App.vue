<template>
  <BlogHeader />

  <ArticleList />

  <BlogFooter />
</template>

<script setup>
import BlogHeader from "./components/BlogHeader.vue"
import BlogFooter from "./components/BlogFooter.vue"
import ArticleList from "./components/ArticleList.vue"
</script>

<style>
#app {
  font-family: Georgia, Arial, sans-serif;
  margin-left: 40px;
  margin-right: 40px;
}
</style>
