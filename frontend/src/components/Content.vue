<template>
  <div class="content">
    <div class="channels__block col-3">
      <ChannelsList v-if="userIsAuthenticated"/>
      <div v-else  class="info__authorization">
        Чтобы начать роботу <span @click="switchLoginModalStatus">Войдите</span> в систему.
      </div>
    </div>
  </div>
</template>

<script>
import ChannelsList from "@/components/ChannelsList";
import {mapGetters, mapMutations} from 'vuex';

export default {
  name: "Content",
  components: {
    ChannelsList
  },

  computed: {
    ...mapGetters(['userIsAuthenticated'])
  },

  methods: {
    ...mapMutations(['switchLoginModalStatus'])
  },
}
</script>

<style scoped>
.content {
  height: 90vh;
  background-color: white;
}

span{
  color: royalblue;
  margin: 0 2px;
}

.info__authorization{
  padding-top: 15px;
  display: flex;
  flex: 0 0 25%;
}

.channels__block {
  border-right: 2px solid rgba(0,0,0,.075);
  height: 100%;
}
</style>