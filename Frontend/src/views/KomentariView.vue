<template>
  <div>
    <span class="text-center" style="margin: 1em">{{ komentari }}</span>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      komentari: "",
    };
  },

  async mounted() {
    let podatci = await fetch("http://localhost:5000/getanje_komentara");
    let rezultati = await podatci.json();
    this.commits = rezultati;
    console.log(rezultati);
    this.komentari = rezultati;
  },

  methods: {},
};
</script>
<style>
div {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Inter", inter;

  height: 0.1px;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}
</style>
