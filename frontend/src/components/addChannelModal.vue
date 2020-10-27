<template>
  <div class="modal__wrapper">
    <div class="modal">
      <div class="modal__inner">
        <h3>Добавление канала</h3>
        <p>Добавьте бота <span>@BotPostram_bot</span> в список администраторов канала с правами на управление постами.
        </p>

        <div class="check_correct">
          <p>Чтобы убедиться в том что вы сделали все правильно, введите название своего в поле.</p>
          <div class="input__wrapper">
            <input type="text" placeholder="@SomeChannel">
          </div>
        </div>
        <div class="button__wrapper">
          <button type="submit">Проверить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddChannelModal"
}
</script>

<style scoped>

h3 {
  text-align: center;
  font-weight: bold;
  margin-bottom: 40px;
}

p {
  font-size: 16px;
  padding: 0 10px 0 10px;
}

span {
  color: blue;
  font-weight: bold;
}

.button__wrapper {
  display: flex;
  justify-content: flex-end;
  margin-top: 45px;
}

.input__wrapper {
}

button {
  text-transform: uppercase;
  padding: 10px;
  border-radius: 8px;
  background-color: #5580a3;
  border: none;
  outline: none;
  color: white;
  font-size: 18px;
}

input {
  font-size: 16px;
  width: 100%;
  outline: none;
  border: none;
  border-bottom: 1px solid rgba(0, 0, 0, 0.5);
}

.modal__wrapper {
  top: 0;
  left: 0;
  position: fixed;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.2);
}

.modal__inner {
  height: 100%;
  padding: 25px;
}

.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  display: block;
  transform: translate(-50%, -50%);
  background-color: white;
  width: 500px;
  height: 350px;
}

</style>