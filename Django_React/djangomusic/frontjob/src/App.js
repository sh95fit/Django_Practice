import React, { Component } from "react";
import { createRoot } from "react-dom/client";


export default class App extends Component{
  constructor(props) {
    super(props);
  }

  render() {
    return <h1>React 연동 화면입니다.</h1>
  }
}

// React 18에 맞는 createRoot 사용  (index.js로 이동)
// const appDiv = document.getElementById("app");
// const root = createRoot(appDiv);  // createRoot로 root 생성
// root.render(<App />);  // root에 App 렌더링