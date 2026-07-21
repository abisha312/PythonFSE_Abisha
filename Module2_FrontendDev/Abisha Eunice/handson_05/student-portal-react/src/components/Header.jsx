function Header({ siteName, enrolledCount }) {
  return (
    <header className="header">
      <h1>{siteName}</h1>

      <nav>
        <ul className="nav-links">
          <li><a href="#">Home</a></li>
          <li><a href="#">Courses</a></li>
          <li><a href="#">Profile</a></li>
        </ul>
      </nav>

      <div className="enrolled-count">
        Enrolled Courses: <strong>{enrolledCount}</strong>
      </div>
    </header>
  );
}

export default Header;