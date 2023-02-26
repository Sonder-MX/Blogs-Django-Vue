<template>
  <BlogHeader></BlogHeader>

  <div id="grid">
    <div id="signup">
      <h3>注册账号</h3>
      <form>
        <div class="form-elem">
          <span>账号：</span>
          <input v-model="signupName" type="text" placeholder="输入用户名" />
        </div>
        <div class="form-elem">
          <span>密码：</span>
          <input v-model="signupPwd" type="password" placeholder="输入密码" />
        </div>
        <div class="form-elem">
          <span>密码：</span>
          <input v-model="againPwd" type="password" placeholder="再次输入密码" />
        </div>
        <div class="form-elem">
          <button type="button" @click.prevent="signup">提交</button>
        </div>
      </form>
      <div class="err-msg" v-show="errorMsg.length > 0">{{ errorMsg }}</div>
    </div>

    <div>
      <!-- 留给后面章节的用户登录 -->
    </div>
  </div>

  <BlogFooter></BlogFooter>
</template>

<script setup>
import BlogHeader from "@/components/BlogHeader.vue"
import BlogFooter from "@/components/BlogFooter.vue"
import { ref } from "vue"
import { sendPostReq } from "@/http"

let signupName = ref("")
let signupPwd = ref("")
let againPwd = ref("")
let signupResponse = ref("")
let errorMsg = ref("")

function signup() {
  if (signupName.value.length > 0 && signupPwd.value.length > 0 && againPwd.value.length > 0) {
    errorMsg.value = ""
    if (signupPwd !== againPwd) {
      againPwd.value = ""
      errorMsg.value = "两次密码不一致，请重新输入！"
      return
    }
    sendPostReq("/user", { username: signupName.value, password: signupPwd.value })
      .then((res) => {
        errorMsg.value = ""
        signupResponse.value = res.data
        alert("注册成功！快去登录吧")
      })
      .catch((_) => (errorMsg.value = "注册失败，请重试！！！"))
  } else {
    errorMsg.value = "输入用户名或密码完成注册！！！"
  }
}

function checkPwd() {
  if (signupPwd !== againPwd) {
    againPwd = ""
    return "两次密码不一致，请重新输入！"
  }
}
</script>

<style scoped>
#grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
#signup {
  text-align: center;
}
.form-elem {
  padding: 10px;
}
input {
  height: 25px;
  padding-left: 10px;
}
button {
  height: 35px;
  cursor: pointer;
  border: none;
  outline: none;
  background: gray;
  color: whitesmoke;
  border-radius: 5px;
  width: 60px;
}

.err-msg {
  color: red;
}
</style>
