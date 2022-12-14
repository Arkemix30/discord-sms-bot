"""second_commit

Revision ID: 2520f2eb8a5a
Revises: 5b0b3fcd6540
Create Date: 2022-08-25 10:57:52.571064

"""
import sqlalchemy as sa
import sqlmodel  # NEW
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "2520f2eb8a5a"
down_revision = "5b0b3fcd6540"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "general_notifications",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column(
            "message",
            sqlmodel.sql.sqltypes.AutoString(length=250),
            nullable=False,
        ),
        sa.Column("sent_at", sa.DateTime(), nullable=True),
        sa.Column(
            "sent_by", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "general_numbers_notifications",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("number_id", sa.Integer(), nullable=True),
        sa.Column("notification_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["notification_id"],
            ["general_notifications.id"],
        ),
        sa.ForeignKeyConstraint(
            ["number_id"],
            ["general_numbers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("notifications")
    op.add_column(
        "general_numbers",
        sa.Column(
            "created_by", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
    )
    op.drop_column("general_numbers", "registered_by")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "general_numbers",
        sa.Column(
            "registered_by", sa.VARCHAR(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("general_numbers", "created_by")
    op.create_table(
        "notifications",
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "message",
            sa.VARCHAR(length=250),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "sent_by", sa.VARCHAR(), autoincrement=False, nullable=True
        ),
        sa.PrimaryKeyConstraint("id", name="notifications_pkey"),
    )
    op.drop_table("general_numbers_notifications")
    op.drop_table("general_notifications")
    # ### end Alembic commands ###
