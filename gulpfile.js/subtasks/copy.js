var gulp = require("gulp"),
    concat = require("gulp-concat"),
    copyTask = function(cb) {
        gulp.src("node_modules/jquery/dist/jquery.min.js")
            .pipe(gulp.dest("src/izi/static/izi/js/jquery"));

        gulp.src("node_modules/bootstrap/less/**/*")
            .pipe(gulp.dest("src/izi/static/izi/less/bootstrap3"));

        gulp.src("node_modules/bootstrap/dist/js/bootstrap.min.js")
            .pipe(gulp.dest("src/izi/static/izi/js/bootstrap3"));

        gulp.src("node_modules/bootstrap/fonts/*")
            .pipe(gulp.dest("src/izi/static/izi/fonts/"));

        gulp.src([
            "node_modules/bootstrap-datetime-picker/js/*.min.js",
            "node_modules/bootstrap-datetime-picker/css/*.min.css"
        ]).pipe(gulp.dest("src/izi/static/izi/js/bootstrap-datetimepicker"));

        gulp.src("node_modules/bootstrap-datetime-picker/js/locales/*")
            .pipe(gulp.dest("src/izi/static/izi/js/bootstrap-datetimepicker/locales"));

        // Concatenate all timepicker locales into a single file for use in the dashboard
        gulp.src("node_modules/bootstrap-datetime-picker/js/locales/*")
            .pipe(concat("bootstrap-datetimepicker.all.js"))
            .pipe(gulp.dest("src/izi/static/izi/js/bootstrap-datetimepicker/locales"));

        gulp.src("node_modules/jquery.inputmask/dist/jquery.inputmask.bundle.js")
            .pipe(gulp.dest("src/izi/static/izi/js/inputmask"));

        gulp.src("node_modules/jquery-mousewheel/jquery.mousewheel.js")
            .pipe(gulp.dest("src/izi/static/izi/js/mousewheel"));

        gulp.src("node_modules/jquery-sortable/source/js/jquery-sortable-min.js")
            .pipe(gulp.dest("src/izi/static/izi/js/jquery-sortable"));

        gulp.src([
            "node_modules/tinymce/**/*.min.js",
            "node_modules/tinymce/**/*.min.css",
            "node_modules/tinymce/**/fonts/*",
            "node_modules/tinymce/**/img/*",
        ]).pipe(gulp.dest("src/izi/static/izi/js/tinymce"));

        gulp.src([
            "node_modules/select2/dist/js/select2.min.js",
            "node_modules/select2/dist/css/select2.min.css"
        ]).pipe(gulp.dest("src/izi/static/izi/js/select2"));

        return gulp.src("node_modules/select2-bootstrap-theme/dist/*.min.css")
            .pipe(gulp.dest("src/izi/static/izi/css"));
    };

gulp.task("copy", copyTask);
