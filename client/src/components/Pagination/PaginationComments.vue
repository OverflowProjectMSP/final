<script>
import Pagination from "vuejs-paginate-next";
export default {
  data() {
    return {
      currentPageNumber: this.currentPage,
    };
  },
  components: {
    Pagination,
  },
  props: {
    currentPage: Number,
    pageCount: Number,
  },
  methods: {
    clickCallback() {
      console.log(
        "Call Back Triggered",
        `Current Page - ${this.currentPageNumber}`
      );
      this.$emit("set-currentpage", this.currentPageNumber);
      console.log(this.currentPage, this.pageCount);
    },
  },
  mounted() {
  },
};
</script>
<template>
  <Pagination
    v-model="currentPageNumber"
    :page-count="pageCount"
    :click-handler="clickCallback"

    :prev-text="'<'"
    :next-text="'>'"
    :container-class="'pagination'"
    :page-class="'page-item'"
    :page-link-class="'page-link'"
    :active-class="'active-page'"
    :prev-class="'prev'"
    :next-class="'next'"
    :hide-prev-next="false"
  />
</template>
<style lang="scss">
.pagination {
  background: white;
  margin: 0px;
  padding: 10px;
  display: flex;
  gap: 5px;
  align-items: center;
  justify-content: center;
  border: none;
  box-sizing: border-box;
  overflow: hidden;
  word-wrap: break-word;
  align-content: center;
}
.page-item {
  display: flex;
  cursor: pointer;
  margin-bottom: 0px;
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently*/
  border-radius: 100%;
}
.page-link {
  border: none !important;
  background-color: #e9e9e9;
  color: #666b85;
  text-align: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border-radius: 50%;
  padding: 10px 15px;
  font-size: 15px;
  font-weight: 550;
  transition: all 0.5s;
  &:hover {
    color: white;
    background-color: #3b82f6 !important;
    border: none;
    transition: none;
    cursor: pointer;
    transition: all 0.5s;
  }
}

.prev a {
  border: none !important;
  background-color: #629bf7 !important;
  color: white !important;
  border-radius: 20px;
  font-size: 15px;
  font-weight: 550;
  cursor: pointer !important;
  user-select: none;
  outline: none !important;
  // &:hover {
  //   color: white;
  //   background-color: #3b85fd !important;
  //   border: none;
  //   transition: none;
  //   cursor: pointer;
  // }
}
.next a {
  border: none !important;
  background-color: #629bf7 !important;
  color: white !important;
  border-radius: 20px;
  font-size: 15px;
  font-weight: 550;
  cursor: pointer;
  user-select: none;
  // &:hover {
  //   color: white;
  //   background-color: #3b85fd !important;
  //   border: none;
  //   transition: none;
  //   cursor: pointer;
  // }
}

.active-page a {
  background-color: #629bf7 !important;
  color: white !important;
  outline: none !important;
  &:hover {
    border: none;
  }
}
.disabled {
  .page-link {
    background-color: #bdc1c5 !important;
  }
  cursor: not-allowed;
}
</style>
