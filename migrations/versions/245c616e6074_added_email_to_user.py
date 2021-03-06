"""added email to user

Revision ID: 245c616e6074
Revises: 55f55c412d93
Create Date: 2020-12-10 02:32:43.355069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '245c616e6074'
down_revision = '55f55c412d93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
