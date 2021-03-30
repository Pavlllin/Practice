class StatsRouter:
    route_app_labels = {'stats'}
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'statistic'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'statistic'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        # if (
        #     obj1._meta.app_label in self.route_app_labels or
        #     obj2._meta.app_label in self.route_app_labels
        # ):
        #    return True
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if db == "statistic":
            if app_label in self.route_app_labels:
                return True
            else:
                return False
        else:
            return app_label not in self.route_app_labels
