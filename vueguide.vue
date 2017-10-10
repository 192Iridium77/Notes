# startup

npm install -g vue-cli
vue init webpack myapp
cy myapp
npm install
npm run dev
npm run build

# Directives

<element v-directiveId="[argument:] expression [| filters...]">
</element>

<span>{{msg}}</span>
<span v-text="msg"></span>
<span v-html="msg"></span>
<span v-once>{{msg}}</span>
<p v-if="show">This is shown</p>
<p v-else>This is not</p>
<p v-show="show">This is shown</p>
<li v-for="user in users">{{user.name}}</li>

data: {
  show: true
  users: [
    {name: 'Bob'},
    {name: 'Kath'}
  ]
}

<div v-bind:class="{active: isActive}"></div>
<div v-bind:style="{color:activeColor}"></div>

data: {
  isActive: true,
    activeColor:'red'
}

# components

Vue.component('my-component', {
  Template: 'this is my component'
})

  <div id="app">
    <my-component></my-component>
  </div>

// reusable code, can be separated into .vue files

