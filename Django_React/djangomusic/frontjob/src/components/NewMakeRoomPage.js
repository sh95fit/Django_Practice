import React, { Component } from "react";

import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import FormHelperText from "@mui/material/FormHelperText";
import FormControl from "@mui/material/FormControl";
import { Link } from "react-router-dom";
import Radio from "@mui/material/Radio";
import RadioGroup from "@mui/material/RadioGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import { Collapse } from "@mui/material";
import { Alert } from "@mui/material";

import { useNavigate } from 'react-router-dom';

// HOC를 이용해 navigate를 props로 전달
function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  }

  return ComponentWithRouterProp;
}



class NewMakeRoomPage extends Component{
  static defaultProps = {
    votesToSkip: 2,
    guestCanPause: true,
    update: false,
    roomTitle: null,
    updateCallback: () => {},
  };

  constructor(props) {
    super(props);
    this.state = {
      guestCanPause: this.props.guestCanPause,
      votesToSkip: this.props.votesToSkip,
      errorMsg: "",
      successMsg: "",
    };

    this.handleRoomButtonPressed = this.handleRoomButtonPressed.bind(this);
    this.handleVotesChange = this.handleVotesChange.bind(this);
    this.handleGuestCanPauseChange = this.handleGuestCanPauseChange.bind(this);
    this.handleUpdateButtonPressed = this.handleUpdateButtonPressed.bind(this);
  }

  handleVotesChange(e){
    this.setState({
      votesToSkip:e.target.value,
    });
  }

  handleGuestCanPauseChange(e){
    this.setState({
      guestCanPause:e.target.value === "true" ? true : false,
    });
  }

  handleRoomButtonPressed(){
    const requestOptions = {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        vote_to_skip: this.state.votesToSkip,
        guest_can_pause: this.state.guestCanPause,
      }),
    };

    fetch("/musicapi/create", requestOptions).then((response)=>response.json()).then((data)=> this.props.navigate("/room/" + data.title));
  }

  handleUpdateButtonPressed(){
    const requestOptions = {
      method: "PATCH",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        vote_to_skip: this.state.votesToSkip,
        guest_can_pause: this.state.guestCanPause,
        title: this.props.roomTitle,
      }),
    };

    fetch("/musicapi/update", requestOptions)
      .then((response) => {
        if (response.ok) {
          this.setState({
            successMsg: "Success Update!"
          });
        } else {
          this.setState({
            errorMsg: "Failed Update..."
          });
        }
        this.props.updateCallback();
      });
      // .then((data)=> this.props.navigate("/room/" + data.title));
  }


  renderCreateButtons() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            onClick={this.handleRoomButtonPressed}
          >
            방 만들기
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button color="secondary" variant="contained" to="/" component={Link}>
            뒤로가기
          </Button>
        </Grid>
      </Grid>
    );
  }

  renderUpdateButton(){
    return (
      <Grid item xs={12} align="center">
        <Button
          color="primary"
          variant="contained"
          onClick={this.handleUpdateButtonPressed}
        >
          Update
        </Button>
      </Grid>
    )
  }

  render() {
    const newtitle = this.props.update ? "🎵Room Update" : "🎵음악 방 만들기";

    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Collapse in={this.state.errorMsg != "" || this.state.successMsg != ""}>
            {this.state.successMsg != "" ? (
              <Alert
                severity="success"
                onClose={() => {
                  this.setState({ successMsg: "" });
                }}
              >
                {this.state.successMsg}
              </Alert>
            ) : (
              <Alert
                severity="error"
                onClose={() => {
                  this.setState({ errorMsg: "" });
                }}
              >
                {this.state.errorMsg}
              </Alert>
            )}
          </Collapse>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
          {newtitle}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl component="fieldset">
            <FormHelperText>
              방문자 재생 상태 제어
            </FormHelperText>
            <RadioGroup
              row
              value={this.state.guestCanPause.toString()}
              // defaultValue={this.props.guestCanPause.toString()}
              onChange={this.handleGuestCanPauseChange}
            >
              <FormControlLabel
                value="true"
                control={<Radio color="primary" />}
                label="연주/중단"
                labelPlacement="bottom"
              />
              <FormControlLabel
                value="false"
                control={<Radio color="secondary" />}
                label="자동"
                labelPlacement="bottom"
              />
            </RadioGroup>
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="number"
              onChange={this.handleVotesChange}
              defaultValue={this.state.votesToSkip}
              inputProps={{
                min: 1,
                style: { textAlign: "center" },
              }}
            />
            <FormHelperText>
              건너 뛰려면 투표가 필요합니다
            </FormHelperText>
          </FormControl>
        </Grid>

        {this.props.update ? this.renderUpdateButton() : this.renderCreateButtons()}
      </Grid>
    );
  }
}

export default withRouter(NewMakeRoomPage);