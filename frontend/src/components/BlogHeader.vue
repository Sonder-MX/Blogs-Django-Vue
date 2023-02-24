<template>
  <div id="header">
    <div class="grid">
      <div></div>
      <h1>My Drf-Vue Blog</h1>
      <div class="search">
        <form>
          <label>
            <input type="text" v-model="searchText" placeholder="输入搜索内容..." />
          </label>
          <button type="button" @click.prevent="searchArticle"></button>
        </form>
      </div>
    </div>
    <hr />
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()
let searchText = ref("")

function searchArticle() {
  if (searchText.value.trim()) {
    router.push({ name: "Home", query: { search: searchText.value.trim() } })
  }
}
</script>

<style scoped>
#header {
  text-align: center;
  margin-top: 20px;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 4fr 1fr;
}

.search {
  padding-top: 22px;
}

* {
  box-sizing: border-box;
}

form {
  position: relative;
  width: 200px;
  margin: 0 auto;
}

input,
button {
  border: none;
  outline: none;
}

input {
  width: 100%;
  height: 35px;
  padding-left: 13px;
  padding-right: 46px;
}

button {
  height: 35px;
  width: 35px;
  cursor: pointer;
  position: absolute;
}

.search input {
  border: 2px solid gray;
  border-radius: 5px;
  background: transparent;
  top: 0;
  right: 0;
}

.search button {
  background: gray;
  border-radius: 0 5px 5px 0;
  width: 45px;
  top: 0;
  right: 0;
}

.search button:before {
  content: "搜索";
  font-size: 13px;
  color: white;
}
</style>
