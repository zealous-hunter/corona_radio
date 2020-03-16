from types import SimpleNamespace


class SubscriptionStorage:

    def findAllSubscriptions(self, cursor, conn):
        cursor.execute('SELECT `id`, `title`, `link`, `created_at`, `updated_at` FROM subscription')
        return [mapToSubscription(record) for record in cursor.fetchall()]

    def saveSubscription(self, cursor, conn, subscription):
        subscription.lastUpdated = datetime.now()
        if hasattr(subscription, 'id'):
            # Update
            cursor.execute('UPDATE subscriptions SET `title`=?, `link`=?, `updated_at`=? WHERE `id`=?', [
                subscription.title,
                subscription.url,
                subscription.id,
                subscription.lastUpdated])
        else:
            # Insert new
            cursor.execute('INSERT INTO subscription (`title`, `link`, `created_at`, `updated_at`) values (?, ?, ?, ?)', [
                subscription.title,
                subscription.link,
                subscription.createdAt,
                subscription.updatedAt])
            subscription.id = cursor.lastrowid
        return subscription

        

def mapToSubscription(record):
    return SimpleNamespace(
        id = record[0],
        title = record[1],
        link = record[2],
        createdAt = record[3],
        updatedAt = record[4])

