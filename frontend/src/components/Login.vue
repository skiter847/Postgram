<template>
  <div class="login">
    <span @click="switchLoginModalStatus">Вход</span>
    <LoginModal v-if="getLoginModalStatus"/>
  </div>
</template>

<script>
import LoginModal from "@/components/LoginModal";
import {mapMutations, mapGetters} from 'vuex';

export default {
  name: "Login",
  components: {
    LoginModal
  },

  computed: {
    ...mapGetters(['getLoginModalStatus'])
  },

  methods: {
    ...mapMutations(['switchLoginModalStatus']),

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