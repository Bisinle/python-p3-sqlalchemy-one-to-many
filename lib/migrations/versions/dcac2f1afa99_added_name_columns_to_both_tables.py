"""added name columns to both tables 

Revision ID: dcac2f1afa99
Revises: d96e1efd510b
Create Date: 2023-08-31 12:51:15.328661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcac2f1afa99'
down_revision = 'd96e1efd510b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_column('title')

    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
