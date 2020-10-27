<template>
  <div class="add-channel">
    <span @click="switchAddChannelStatus"> + Добавить канал</span>
    <addChannelModal v-if="getAddChannelModalStatus"/>
  </div>
</template>

<script>
import addChannelModal from "@/components/addChannelModal";
import {mapGetters, mapMutations} from 'vuex';

export default {
  name: "ChannelsList",
  components: {
    addChannelModal
  },

  computed:{
    ...mapGetters(['getAddChannelModalStatus'])
  },

  methods: {
    ...mapMutations(['switchAddChannelStatus'])
  },

}
</script>

<style scoped>

.add-channel {
  padding-top: 10px;
  display: flex;
  flex: 0 0 25%;
  justify-content: center;
}

.add-channel span {
  font-size: 15px;
  padding: 10px 25px 10px 25px;
  color: white;
  font-weight: bold;
  background-color: #5580a3;
  cursor: pointer;
}

.add-channel span:hover {
  background-color: #497799;
}

</style>