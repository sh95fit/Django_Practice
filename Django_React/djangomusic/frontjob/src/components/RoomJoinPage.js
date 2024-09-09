import React, { Component } from "react";

import { TextField, Button, Grid, Typography } from "@mui/material";
import { Link } from "react-router-dom"

import { useNavigate } from 'react-router-dom';

// HOC를 이용해 navigate를 props로 전달
function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  }

  return ComponentWithRouterProp;
}



class RoomJoinPage extends Component{
  constructor(props) {
    super(props);
    this.state = {
      roomTitle: "",
      error: "",
    };

    this.handleTextFieldChange = this.handleTextFieldChange.bind(this);
    this.roomButtonPressed = this.roomButtonPressed.bind(this);
  }

  render() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            Join in the Room
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <TextField
            error={Boolean(this.state.error)}
            label="Room Name"
            placeholder="Enter the Room Name"
            value={this.state.roomTitle}
            helperText={this.state.error}
            variant="outlined"
            onChange = {this.handleTextFieldChange}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="primary"
            onClick = {this.roomButtonPressed}
          >입장하기</Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            component={Link} to= "/"
          >뒤로가기</Button>
        </Grid>
      </Grid>
    )
  }

  handleTextFieldChange(e){
    this.setState({
      roomTitle: e.target.value,
    });
  }

  roomButtonPressed() {
    // console.log(this.state.roomTitle);
    const requestOptions = {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        title: this.state.roomTitle,
      }),
    };
    fetch("musicapi/join", requestOptions).then((response) => {
      if (response.ok) {
        this.props.navigate(`/room/${this.state.roomTitle}`);
      } else {
        this.setState({ error: "Not Found Room..."});
      }
    })
    .catch((error) => {
      console.log(error);
    })
  }

  handle
}


export default withRouter(RoomJoinPage);