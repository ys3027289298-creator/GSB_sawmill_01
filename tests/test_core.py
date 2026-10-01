import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_duplicate_enqueue_rejected(self):
        state = core.new_game()
        self.assertTrue(core.enqueue(state, 1))
        self.assertFalse(core.enqueue(state, 1))

    def test_02_capacity_limit(self):
        state = core.new_game()
        self.assertTrue(core.enqueue(state, 1))
        self.assertTrue(core.enqueue(state, 2))
        self.assertFalse(core.enqueue(state, 3))

    def test_03_empty_dequeue_none(self):
        state = core.new_game()
        self.assertIsNone(core.dequeue(state))

    def test_04_fifo_order(self):
        state = core.new_game()
        core.enqueue(state, 1)
        core.enqueue(state, 2)
        self.assertEqual(core.dequeue(state), 1)

    def test_05_paused_blocks_dequeue(self):
        state = core.new_game()
        core.enqueue(state, 1)
        state["paused"] = True
        self.assertIsNone(core.dequeue(state))

    def test_06_peek_keeps_item(self):
        state = core.new_game()
        core.enqueue(state, 1)
        self.assertEqual(core.peek(state), 1)
        self.assertEqual(core.size(state), 1)

    def test_07_size_count(self):
        state = core.new_game()
        core.enqueue(state, 1)
        self.assertEqual(core.size(state), 1)

    def test_08_process_once(self):
        state = core.new_game()
        core.process(state)
        self.assertEqual(state["processed"], 1)

    def test_09_reset_clears_stats(self):
        state = core.new_game()
        state["processed"] = 5
        core.reset(state)
        self.assertEqual(state["processed"], 0)

    def test_10_load_preserves_id(self):
        state = core.new_game()
        state["next_id"] = 7
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["next_id"], 7)


if __name__ == "__main__":
    unittest.main()
