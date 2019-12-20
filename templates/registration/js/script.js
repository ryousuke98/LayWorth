class MenuLinks extends React.Component {
  constructor(props) {
    super(props);
    // Any number of links can be added here
    this.state = {
      links: [{
          text: 'Home',
          link: 'test.html',
          icon: 'fa fa-home' },
          {
        text: 'ユーザ',
        link: 'https://ja.wikipedia.org/wiki/%E7%AF%84%E9%A6%AC%E5%8B%87%E6%AC%A1%E9%83%8E',
        icon: 'fa fa-user' },
        {
        text: 'タスク作成',
        link: 'http://www.riccardotartaglia.it/jkanban/',
        icon: 'fa fa-pencil-square-o' },
          {
            text: '設定',
            link: 'settings.html',
            icon: 'fa fa-cog' },
        {
        text: 'サインアウト',
        link: 'index.html',
        icon: 'fa fa-user-times' }] };


  }
  render() {
    let links = this.state.links.map((link, i) => React.createElement("li", { ref: i + 1 }, React.createElement("i", { "aria-hidden": "true", className: `fa ${link.icon}` }), React.createElement("a", { href: link.link, target: "_blank" }, link.text)));

    return (
      React.createElement("div", { className: this.props.menuStatus, id: "menu" },
      React.createElement("ul", null,
      links)));



  }}


class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false };

    this._menuToggle = this._menuToggle.bind(this);
    this._handleDocumentClick = this._handleDocumentClick.bind(this);
  }
  componentDidMount() {
    document.addEventListener('click', this._handleDocumentClick, false);
  }
  componentWillUnmount() {
    document.removeEventListener('click', this._handleDocumentClick, false);
  }
  _handleDocumentClick(e) {
    if (!this.refs.root.contains(e.target) && this.state.isOpen === true) {
      this.setState({
        isOpen: false });

    };
  }
  _menuToggle(e) {
    e.stopPropagation();
    this.setState({
      isOpen: !this.state.isOpen });

  }
  render() {
    let menuStatus = this.state.isOpen ? 'isopen' : '';

    return (
      React.createElement("div", { ref: "root" },
      React.createElement("div", { className: "menubar" },
      React.createElement("div", { className: "hambclicker", onClick: this._menuToggle }),
      React.createElement("div", { id: "hambmenu", className: menuStatus }, React.createElement("span", null), React.createElement("span", null), React.createElement("span", null), React.createElement("span", null)),
      React.createElement("div", { className: "title" },
      React.createElement("span", null, this.props.title))),


      React.createElement(MenuLinks, { menuStatus: menuStatus })));


  }}


ReactDOM.render(React.createElement(Menu, { title: "Lay Worth" }), document.getElementById('app'));