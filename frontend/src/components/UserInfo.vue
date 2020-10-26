<template>
  <div class="user">
    <div class="user__picture">
      <img src="@/assets/img/userpic.jpeg" alt="" style="width: 30px; height: 30px; border-radius: 50%">
    </div>
    <div class="user__username">{{ getUserData.first_name }}</div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex';

export default {
  name: "UserInfo",

  computed: {
    ...mapGetters(['getUserData'])
  },
}
</script>

<style scoped>
.user{
  display: flex;
}

.user__picture{
  margin-right: 5px;
}

.user__username{
  font-size: 15px;
  margin-top: 4%;
}
</style>