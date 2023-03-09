<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row">
          <input type="text" class="form-control col me-2 mb-5" placeholder="Name" v-model='s.name' />
          <input type="text" class="form-control col me-2 mb-5" placeholder="Email" v-model='s.email' />
          <input type="text" class="form-control col me-2 mb-5" placeholder="Rating" v-model='s.rating' />
        <button class="btn btn-success col mb-5">Submit</button>
      </div>
    </form>

    <table class="table text-center">
      <thead>
        <th>Name</th>
        <th>Email</th>
        <th>Raing</th>
      </thead>
      <tbody>
        <tr :key='s.id' v-for="s in s_list" @dblclick="$data.s = s">
          <td>{{ s.name }}</td>
          <td>{{ s.email }}</td>
          <td>{{ s.rating }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteList(s)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'App',
  componets: {},
  data() {
    return {
      s: {},
      // name: '',
      // email: '',
      // rating: ''
      // },
      s_list: []
    }
  },
  setup() {},
  async created() {
    // const response = await fetch('http://127.0.0.1:8000/api/s_list/')
    // this.s_list = await response.json()
    await this.getList()
  },
  mounted() {},
  unmounted() {},
  methods: {
    submitForm() {
      if (this.s.id === undefined) {
        this.createList()
      } else {
        this.editList()
      }
    },

    async getList() {
      const response = await fetch('http://127.0.0.1:8000/api/s_list/')
      this.s_list = await response.json()
    },

    async createList() {
      await this.getList()

      await fetch('http://127.0.0.1:8000/api/s_list/', {
      // const response = await fetch('http://127.0.0.1:8000/api/s_list/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.s)
      })

      // this.s_list.push(await response.json())
      await this.getList()
    },

    async editList() {
      await this.getList()

      await fetch(`http://127.0.0.1:8000/api/s_list/${this.s.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.s)
      })

      await this.getList()
      this.s = {}
    },

    async deleteList(s) {
      await fetch(`http://127.0.0.1:8000/api/s_list/${s.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.s)
      })

      await this.getList()
    }
  }
}
</script>
