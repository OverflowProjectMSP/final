<script>
import axios from "axios";
export default {
  components: {
    // QuestionItem,
  },
  data() {
    return {
      $axios: axios,
      questions: [], // Массив вопросов
      currentPage: 1, // Номер текущей страницы
      questionsPerPage: 5, // Количество вопросов на странице
      totalQuestions: 0, // Общее количество вопросов
      totalPages: 0, // Общее количество страниц
      maxVisiblePages: 4, // Максимальное количество отображаемых номеров страниц
    };
  },
  mounted() {
    this.loadQuestions(2); // Загрузка первой страницы при монтировании компонента
  },
  computed: {
    visiblePages() {
      const pages = [];
      // Отображаем 4 страницы, но если меньше, то все
      const start = Math.max(1, this.currentPage - 1);
      const end = Math.min(this.totalPages, this.currentPage + 2);

      // Если общее количество страниц меньше, чем maxVisiblePages,
      // отображаем все страницы
      if (this.totalPages <= this.maxVisiblePages) {
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
      } else {
        for (let i = start; i <= end; i++) {
          pages.push(i);
        }
      }

      return pages;
    },
    showDotsLeft() {
      return this.currentPage > this.maxVisiblePages + 1;
    },
    showDotsRight() {
      return this.currentPage + this.maxVisiblePages < this.totalPages;
    },
  },
  methods: {
    loadQuestions(page) {
      this.currentPage = page;
      const start = page * this.questionsPerPage - this.questionsPerPage + 1; // Начало интервала
      const end = page * this.questionsPerPage + 1; // Конец интервала
      // Отправка запроса на бекенд с интервалом start-end
      console.log(start, end);
      this.getQuestions(start, end);
    },
    async getQuestions(start, end) {
      try {
        const res = await axios.get(
          `https://api.upfollow.ru/get-questions?start=${start}&end=${end}`
        );
        this.questions = res.data;
        console.log(this.questions)
        this.totalQuestions = res.data.count; // Получение общего количества вопросов от бекенда
        this.totalPages = Math.ceil(
          this.totalQuestions / this.questionsPerPage
        ); // Обновление общего количества страниц
      } catch (err) {}
    },

    loadPage(page) {
      this.loadQuestions(page);
    },
    loadPreviousPage() {
      if (this.currentPage > 1) {
        this.loadQuestions(this.currentPage - 1);
      }
    },
    loadNextPage() {
      if (this.currentPage * this.questionsPerPage < this.totalQuestions) {
        this.loadQuestions(this.currentPage + 1);
      }
    },
    handleDotsClick(direction) {
      if (direction === "left") {
        this.loadPage(this.currentPage - this.maxVisiblePages); // Переход на первую страницу из видимого диапазона
      } else if (direction === "right") {
        this.loadPage(this.currentPage + this.maxVisiblePages); // Переход на последнюю страницу из видимого диапазона
      }
    },
  },
};
</script>
<template>
  <div class="pagination">
    <ul>
      {{ questions }}
    </ul>
    <div class="pagination-controls">
      <button @click="loadPreviousPage" :disabled="currentPage === 1">
        Предыдущая
      </button>
      <span v-if="showDotsLeft" class="dots" @click="handleDotsClick('left')"
        >...</span
      >
      <span
        v-for="page in visiblePages"
        :key="page"
        :class="{ active: page === currentPage }"
        @click="loadPage(page)"
      >
        {{ page }}
      </span>
      <span v-if="showDotsRight" class="dots" @click="handleDotsClick('right')"
        >...</span
      >
      <button @click="loadNextPage" :disabled="currentPage === totalPages">
        Следующая
      </button>
    </div>
  </div>
</template>

<style scoped>
.pagination {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.pagination-controls {
  display: flex;
  margin-top: 10px;
}

.dots {
  margin: 0 5px;
  cursor: pointer;
  color: #333;
}

.dots:hover {
  text-decoration: underline;
}

.active {
  font-weight: bold;
  color: #007bff; /* Синий цвет для активной страницы */
}
</style>
