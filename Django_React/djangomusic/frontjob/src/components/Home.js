import React, { Component } from "react";

import RoomJoinPage from "./RoomJoinPage";
import NewMakeRoomPage from "./NewMakeRoomPage";
// import Room from "./Room";
import RoomWrapper from "./RoomWrapper";

import {BrowserRouter as Router, Route, Routes, Link, Navigate} from "react-router-dom";

import { TextField, Button, Grid, Typography, ButtonGroup } from "@mui/material";

export default class Home extends Component{
  constructor(props) {
    super(props);
    this.state = {
      roomTitle:null,
    };
  }

  async componentDidMount() {
    fetch("/musicapi/userin")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          roomTitle: data.title,
        })
      })
  }

  renderHomePage(){
    return(
      <Grid container spacing={3}>
        <Grid item xs={12} align="center">
          <Typography variant="h3" compact="h3">
          HomePage Hall
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <ButtonGroup disableElevation variant="contained" color="primary">
            <Button color="primary" to="/join" component={Link}>
              Sign UP
            </Button>
            <Button color="secondary" to="/create" component={Link}>
              Make Room
            </Button>
          </ButtonGroup>
        </Grid>
      </Grid>
    );
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={
              this.state.roomTitle ? (
                <Navigate to={`/room/${this.state.roomTitle}`} />
              ) : (
                this.renderHomePage()
              )
          } />
          <Route path="/join" element={<RoomJoinPage/>}></Route>
          <Route path="/create" element={<NewMakeRoomPage/>}></Route>
          {/* <Route path="/room/:roomTitle" element={<Room/>}></Route> */}
          <Route path="/room/:roomTitle" element={<RoomWrapper/>}></Route>
        </Routes>
      </Router>
    )
  }

}