<template>
  <div class="login">
    <span @click="showModalWindow">Вход</span>
    <LoginModal v-if="showModal"/>
  </div>
</template>

<script>
import LoginModal from "@/components/LoginModal";

export default {
  name: "Login",
  components: {
    LoginModal
  },

  data() {
    return {
      showModal: false,
    }
  },
  methods: {
    showModalWindow() {
      this.showModal = true
      console.log(this.showModal)
    }
  },
}

</script>

<style scoped>
.header__auth-menu span {
  color: white;
  font-size: 20px;
  text-decoration: none;

}
</style>