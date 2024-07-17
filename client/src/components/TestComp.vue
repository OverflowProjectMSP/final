<template>
  <div>
    <textarea ref="textArea" v-model="text" @input="updateCursor" @click="updateCursor"></textarea>
    <button @click="addBoldTag">B</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: '',
      cursorPosition: 0
    };
  },
  methods: {
    updateCursor(event) {
      this.cursorPosition = event.target.selectionStart;
    },
    addBoldTag() {
      const beforeCursor = this.text.slice(0, this.cursorPosition);
      const afterCursor = this.text.slice(this.cursorPosition);

      this.text = `${beforeCursor}<b></b>${afterCursor}`;
      this.$nextTick(() => {
        const newCursorPosition = this.cursorPosition + 3; // Позиция курсора между тегами <b>|</b>
        this.$refs.textArea.focus();
        this.$refs.textArea.setSelectionRange(newCursorPosition, newCursorPosition);
        this.updateCursor({target: this.$refs.textArea});
      });
    }
  }
};
</script>

<style scoped>
textarea {
  width: 100%;
  height: 100px;
}
</style>