<template>
  <router-view></router-view>
</template>

<script setup></script>

<style>
#app {
  font-family: Georgia, Arial, sans-serif;
  margin-left: 40px;
  margin-right: 40px;
}

html::-webkit-scrollbar {
  width: 10px;
  height: 10px;
  background-color: #f5f5f5;
}

html::-webkit-scrollbar-thumb {
  border-radius: 4px;
  background-color: #c0c4cc;
}

html::-webkit-scrollbar-track {
  border-radius: 4px;
  background-color: #f5f5f5;
}

/* firefox scrollbar */
html {
  scrollbar-width: thin;
  scrollbar-color: #c0c4cc #f5f5f5;
}
</style>
